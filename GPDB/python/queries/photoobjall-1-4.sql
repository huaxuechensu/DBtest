-- Q9
explain analyze Select 
	G.objID, G.u, G.g, G.r, G.i, G.z 
from 
	PhotoObjAll_1 as G, Star_1 as S 
where 
	G.parentID > 0 and G.parentID = S.parentID;
