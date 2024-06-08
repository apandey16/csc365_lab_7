gatherRevenue = """ with CarryOversEnd as (
    select Room, MONTH(CheckIn) as Month, sum(DATEDIFF(LAST_DAY(CheckIn), CheckIn) * Rate) as monthlyCostEndMonth from lab7_reservations
    where YEAR(CheckIn) = YEAR(CURDATE()) and MONTH(CheckIn) != MONTH(CheckOut)
    group by Room, MONTH(CheckIn)
    order by Room, MONTH(CheckIn)
), CarryOversStart as (
    select Room, MONTH(CheckOut) as Month, sum(DAY(CheckOut) * Rate) as monthlyCostStartMonth from lab7_reservations
    where YEAR(CheckIn) = YEAR(CURDATE()) and DAY(CheckIn) > DAY(CheckOut)
    group by Room, MONTH(CheckOut)
    order by Room, MONTH(CheckOut)
), SameMonth as (
    select Room, MONTH(CheckIn) as Month, sum(DATEDIFF(CheckOut, CheckIn) * Rate) as monthlyCostSameMonth from lab7_reservations
    where YEAR(CheckIn) = YEAR(CURDATE()) and MONTH(CheckIn) = MONTH(CheckOut)
    group by Room, MONTH(CheckIn)
    order by Room, MONTH(CheckIn)
)
select SameMonth.Room, SameMonth.Month, coalesce(monthlyCostStartMonth, 0) + monthlyCostSameMonth + coalesce(monthlyCostEndMonth, 0) as monthlyCost from SameMonth left outer join CarryOversStart on CarryOversStart.Room = SameMonth.Room and CarryOversStart.Month = SameMonth.Month left outer join CarryOversEnd on CarryOversEnd.Room = SameMonth.Room and CarryOversEnd.Month = SameMonth.Month
order by SameMonth.Room, SameMonth.Month """