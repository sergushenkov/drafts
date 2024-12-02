-- Задание 1
select
    squad_id,
    name
from Squads
where leader_id is null;

-- Задание 2
select 
    dwarf_id,
    name
from Dwarves
where profession = 'Warrior'
and age > 150;

-- Задание 3
select 
    d.dwarf_id,
    d.name
from Dwarves d
join Items i on i.owner_id = d.dwarf_id
where i.type = 'weapon'
group by d.dwarf_id, d.name;

-- Задание 4
select 
    d.dwarf_id,
    d.name,
    t.status,
    count(task_id)
from Dwarves d
left join Tasks t on d.dwarf_id = t.assigned_to
group by d.dwarf_id, d.name, t.status;

-- Задание 5
select 
    t.task_id,
    t.description
from Dwarves d
join Squads s on d.squad_id = s.squad_id and s.name = 'Guardians'
left join Tasks t on d.dwarf_id = t.assigned_to;

-- Задание 6
select 
    d.dwarf_id,
    d.name,
    r.relationship,
    d1.dwarf_id as partner_id,
    d1.name partner_name,
from Dwarves d
left join Relationships r on d.dwarf_id = r.dwarf_id
left join Dwarfes d1 on d1.dwarf_id = r.related_to;
