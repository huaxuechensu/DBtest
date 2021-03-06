-- Find all galaxies without saturated pixels within 1' of a given point.

-- 输出查询结果到文件
\o /tmp/Q1.txt

create or replace function fQ1()
returns setof text
as $$
declare saturated bigint;
begin
saturated := fPhotoFlags('saturated');
return query explain analyze select G.objID, GN.distance
from Galaxy as G join fGetNearbyObjEq(185,-0.5, 1) as GN
on G.objID = GN.objID
where (G.flags & saturated) = 0
order by distance;
end;
$$ language plpgsql;

select fQ1();

/*
tables:
DataConstants

views:

functions: 
fPhotoFlags
fGetNearbyObjEq
fGetNearbyObjXYZ
fHtmCoverCircleXyz
*/
