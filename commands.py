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

gatherRoomsList = """
with popularity as (
    select Room, ROUND((sum(DATEDIFF(Checkout, GREATEST(CheckIn, DATE_SUB(CURDATE(), INTERVAL 180 DAY))))/180)*100, 2) as Popularity from lab7_reservations
    where DATEDIFF(CURDATE(), Checkout) <= 180
    group by Room
    order by Popularity desc
), recentStay as (
    select Room, min(Checkout) as earliestOpening from lab7_reservations
    where Checkout >= CURDATE()
    group by Room),
recentLength as (
    select r.Room, DATEDIFF(r.Checkout, r.CheckIn) AS lengthOfRecentStay 
    from 
        lab7_reservations r
    join 
        (select 
             Room, 
             MAX(Checkout) AS MaxCheckout 
         from 
             lab7_reservations 
         where 
             Checkout <= CURDATE() 
         group by
             Room) as max_checkouts
    on 
    r.Room = max_checkouts.Room and r.Checkout = max_checkouts.MaxCheckout
)
select Room, RoomName, Beds, bedType, maxOcc, basePrice, decor, Popularity, earliestOpening, lengthOfRecentStay from popularity natural join recentStay natural join recentLength join lab7_rooms on lab7_rooms.RoomCode = popularity.Room
order by popularity.Popularity desc
"""