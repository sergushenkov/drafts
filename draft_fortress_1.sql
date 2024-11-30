-- задача 1
select
    d.dwarf_id,
    d.name as dwarf_name,
    d.squad_id,
    s.name as squad_name
from Dwarves d
join Squads s on d.squad_id = s.squad_id
order by squad_id, dwarf_id;

-- задача 2
select
    d.dwarf_id,
    d.name as dwarf_name
from Dwarves d
where d.profession = 'minner'
and d.squad_id is null
order by dwarf_id;

-- задача 3
select 
    task_id,
    description
from (
    select
        task_id,
        description,
        range() over(order by priority asc) as rn
    from Tasks t
    where status = 'pending'
) t
where rn = 1;

-- задача 4
select
    d.dwarf_id,
    d.name,
    count(item_id)
from Dwarves d
join Items i on d.dwarf_id = i.owner_id
group by d.dwarf_id, d.name;

-- задача 5
select
    s.squad_id,
    s.name,
    count(*)
from Squads s
left join Dwarves d on s.squad_id = d.squad_id
group by s.squad_id, s.name;

-- задача 6
select t.profession
from (
    select 
        t.profession,
        range() over(order by t.cnt desc) as rn
    from (
        select 
            d.profession,
            count(t.task_id) cnt
        from Dwarves d
        join Tasks t on d.dwarf_id = t.assigned_to
        where t.status in ('pending', 'in_progress')
        group by d.profession
    ) t
) t
where rn = 1;

-- задача 7
select
    i.type,
    avg(d.age)
from Items i
left join Dwarves d on d.dwarf_id = i.owner_id;

-- задача 8
with t as (
    select avg(age) as avg_age from Dwarves
)
select
    d.dwarf_id,
    d.name as dwarf_name
from Dwarves d
left join Items i on d.dwarf_id = i.owner_id
join t.avg_age on 1 = 1
where i.owner_id is null
and d.age > t.avg_age;
