-- Q5-1
-- reduce the number of where clause
explain analyze SELECT 
	g1.objID,g2.objID 
FROM 
	Galaxy AS g1 JOIN neighbors AS N ON g1.objID = N.objID JOIN Galaxy AS g2 ON g2.objID = N.NeighborObjID 
WHERE
	g1.objID < g2.objID and 
	N.neighborType = 3 and 
	g1.petroRad_u > 0 and 
	g2.petroRad_u > 0 and 
	g1.petroRad_g > 0 and
	(N.distance <= (g1.petroR50_r + g2.petroR50_r));
