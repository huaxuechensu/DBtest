CREATE external TABLE public.PhotoObjAll_ext(
	objID bigint ,
	skyVersion smallint ,
	run smallint ,
	rerun smallint ,
	camcol smallint ,
	field smallint ,
	obj smallint ,
	mode smallint ,
	nChild smallint ,
	type smallint ,
	clean int ,
	probPSF real ,
	insideMask smallint ,
	flags bigint ,
	rowc real ,
	rowcErr real ,
	colc real ,
	colcErr real ,
	rowv real ,
	rowvErr real ,
	colv real ,
	colvErr real ,
	rowc_u real ,
	rowc_g real ,
	rowc_r real ,
	rowc_i real ,
	rowc_z real ,
	rowcErr_u real ,
	rowcErr_g real ,
	rowcErr_r real ,
	rowcErr_i real ,
	rowcErr_z real ,
	colc_u real ,
	colc_g real ,
	colc_r real ,
	colc_i real ,
	colc_z real ,
	colcErr_u real ,
	colcErr_g real ,
	colcErr_r real ,
	colcErr_i real ,
	colcErr_z real ,
	sky_u real ,
	sky_g real ,
	sky_r real ,
	sky_i real ,
	sky_z real ,
	skyIvar_u real ,
	skyIvar_g real ,
	skyIvar_r real ,
	skyIvar_i real ,
	skyIvar_z real ,
	psfMag_u real ,
	psfMag_g real ,
	psfMag_r real ,
	psfMag_i real ,
	psfMag_z real ,
	psfMagErr_u real ,
	psfMagErr_g real ,
	psfMagErr_r real ,
	psfMagErr_i real ,
	psfMagErr_z real ,
	fiberMag_u real ,
	fiberMag_g real ,
	fiberMag_r real ,
	fiberMag_i real ,
	fiberMag_z real ,
	fiberMagErr_u real ,
	fiberMagErr_g real ,
	fiberMagErr_r real ,
	fiberMagErr_i real ,
	fiberMagErr_z real ,
	fiber2Mag_u real ,
	fiber2Mag_g real ,
	fiber2Mag_r real ,
	fiber2Mag_i real ,
	fiber2Mag_z real ,
	fiber2MagErr_u real ,
	fiber2MagErr_g real ,
	fiber2MagErr_r real ,
	fiber2MagErr_i real ,
	fiber2MagErr_z real ,
	petroMag_u real ,
	petroMag_g real ,
	petroMag_r real ,
	petroMag_i real ,
	petroMag_z real ,
	petroMagErr_u real ,
	petroMagErr_g real ,
	petroMagErr_r real ,
	petroMagErr_i real ,
	petroMagErr_z real ,
	psfFlux_u real ,
	psfFlux_g real ,
	psfFlux_r real ,
	psfFlux_i real ,
	psfFlux_z real ,
	psfFluxIvar_u real ,
	psfFluxIvar_g real ,
	psfFluxIvar_r real ,
	psfFluxIvar_i real ,
	psfFluxIvar_z real ,
	fiberFlux_u real ,
	fiberFlux_g real ,
	fiberFlux_r real ,
	fiberFlux_i real ,
	fiberFlux_z real ,
	fiberFluxIvar_u real ,
	fiberFluxIvar_g real ,
	fiberFluxIvar_r real ,
	fiberFluxIvar_i real ,
	fiberFluxIvar_z real ,
	fiber2Flux_u real ,
	fiber2Flux_g real ,
	fiber2Flux_r real ,
	fiber2Flux_i real ,
	fiber2Flux_z real ,
	fiber2FluxIvar_u real ,
	fiber2FluxIvar_g real ,
	fiber2FluxIvar_r real ,
	fiber2FluxIvar_i real ,
	fiber2FluxIvar_z real ,
	petroFlux_u real ,
	petroFlux_g real ,
	petroFlux_r real ,
	petroFlux_i real ,
	petroFlux_z real ,
	petroFluxIvar_u real ,
	petroFluxIvar_g real ,
	petroFluxIvar_r real ,
	petroFluxIvar_i real ,
	petroFluxIvar_z real ,
	petroRad_u real ,
	petroRad_g real ,
	petroRad_r real ,
	petroRad_i real ,
	petroRad_z real ,
	petroRadErr_u real ,
	petroRadErr_g real ,
	petroRadErr_r real ,
	petroRadErr_i real ,
	petroRadErr_z real ,
	petroR50_u real ,
	petroR50_g real ,
	petroR50_r real ,
	petroR50_i real ,
	petroR50_z real ,
	petroR50Err_u real ,
	petroR50Err_g real ,
	petroR50Err_r real ,
	petroR50Err_i real ,
	petroR50Err_z real ,
	petroR90_u real ,
	petroR90_g real ,
	petroR90_r real ,
	petroR90_i real ,
	petroR90_z real ,
	petroR90Err_u real ,
	petroR90Err_g real ,
	petroR90Err_r real ,
	petroR90Err_i real ,
	petroR90Err_z real ,
	q_u real ,
	q_g real ,
	q_r real ,
	q_i real ,
	q_z real ,
	qErr_u real ,
	qErr_g real ,
	qErr_r real ,
	qErr_i real ,
	qErr_z real ,
	u_u real ,
	u_g real ,
	u_r real ,
	u_i real ,
	u_z real ,
	uErr_u real ,
	uErr_g real ,
	uErr_r real ,
	uErr_i real ,
	uErr_z real ,
	mE1_u real ,
	mE1_g real ,
	mE1_r real ,
	mE1_i real ,
	mE1_z real ,
	mE2_u real ,
	mE2_g real ,
	mE2_r real ,
	mE2_i real ,
	mE2_z real ,
	mE1E1Err_u real ,
	mE1E1Err_g real ,
	mE1E1Err_r real ,
	mE1E1Err_i real ,
	mE1E1Err_z real ,
	mE1E2Err_u real ,
	mE1E2Err_g real ,
	mE1E2Err_r real ,
	mE1E2Err_i real ,
	mE1E2Err_z real ,
	mE2E2Err_u real ,
	mE2E2Err_g real ,
	mE2E2Err_r real ,
	mE2E2Err_i real ,
	mE2E2Err_z real ,
	mRrCc_u real ,
	mRrCc_g real ,
	mRrCc_r real ,
	mRrCc_i real ,
	mRrCc_z real ,
	mRrCcErr_u real ,
	mRrCcErr_g real ,
	mRrCcErr_r real ,
	mRrCcErr_i real ,
	mRrCcErr_z real ,
	mCr4_u real ,
	mCr4_g real ,
	mCr4_r real ,
	mCr4_i real ,
	mCr4_z real ,
	mE1PSF_u real ,
	mE1PSF_g real ,
	mE1PSF_r real ,
	mE1PSF_i real ,
	mE1PSF_z real ,
	mE2PSF_u real ,
	mE2PSF_g real ,
	mE2PSF_r real ,
	mE2PSF_i real ,
	mE2PSF_z real ,
	mRrCcPSF_u real ,
	mRrCcPSF_g real ,
	mRrCcPSF_r real ,
	mRrCcPSF_i real ,
	mRrCcPSF_z real ,
	mCr4PSF_u real ,
	mCr4PSF_g real ,
	mCr4PSF_r real ,
	mCr4PSF_i real ,
	mCr4PSF_z real ,
	deVRad_u real ,
	deVRad_g real ,
	deVRad_r real ,
	deVRad_i real ,
	deVRad_z real ,
	deVRadErr_u real ,
	deVRadErr_g real ,
	deVRadErr_r real ,
	deVRadErr_i real ,
	deVRadErr_z real ,
	deVAB_u real ,
	deVAB_g real ,
	deVAB_r real ,
	deVAB_i real ,
	deVAB_z real ,
	deVABErr_u real ,
	deVABErr_g real ,
	deVABErr_r real ,
	deVABErr_i real ,
	deVABErr_z real ,
	deVPhi_u real ,
	deVPhi_g real ,
	deVPhi_r real ,
	deVPhi_i real ,
	deVPhi_z real ,
	deVMag_u real ,
	deVMag_g real ,
	deVMag_r real ,
	deVMag_i real ,
	deVMag_z real ,
	deVMagErr_u real ,
	deVMagErr_g real ,
	deVMagErr_r real ,
	deVMagErr_i real ,
	deVMagErr_z real ,
	deVFlux_u real ,
	deVFlux_g real ,
	deVFlux_r real ,
	deVFlux_i real ,
	deVFlux_z real ,
	deVFluxIvar_u real ,
	deVFluxIvar_g real ,
	deVFluxIvar_r real ,
	deVFluxIvar_i real ,
	deVFluxIvar_z real ,
	expRad_u real ,
	expRad_g real ,
	expRad_r real ,
	expRad_i real ,
	expRad_z real ,
	expRadErr_u real ,
	expRadErr_g real ,
	expRadErr_r real ,
	expRadErr_i real ,
	expRadErr_z real ,
	expAB_u real ,
	expAB_g real ,
	expAB_r real ,
	expAB_i real ,
	expAB_z real ,
	expABErr_u real ,
	expABErr_g real ,
	expABErr_r real ,
	expABErr_i real ,
	expABErr_z real ,
	expPhi_u real ,
	expPhi_g real ,
	expPhi_r real ,
	expPhi_i real ,
	expPhi_z real ,
	expMag_u real ,
	expMag_g real ,
	expMag_r real ,
	expMag_i real ,
	expMag_z real ,
	expMagErr_u real ,
	expMagErr_g real ,
	expMagErr_r real ,
	expMagErr_i real ,
	expMagErr_z real ,
	modelMag_u real ,
	modelMag_g real ,
	modelMag_r real ,
	modelMag_i real ,
	modelMag_z real ,
	modelMagErr_u real ,
	modelMagErr_g real ,
	modelMagErr_r real ,
	modelMagErr_i real ,
	modelMagErr_z real ,
	cModelMag_u real ,
	cModelMag_g real ,
	cModelMag_r real ,
	cModelMag_i real ,
	cModelMag_z real ,
	cModelMagErr_u real ,
	cModelMagErr_g real ,
	cModelMagErr_r real ,
	cModelMagErr_i real ,
	cModelMagErr_z real ,
	expFlux_u real ,
	expFlux_g real ,
	expFlux_r real ,
	expFlux_i real ,
	expFlux_z real ,
	expFluxIvar_u real ,
	expFluxIvar_g real ,
	expFluxIvar_r real ,
	expFluxIvar_i real ,
	expFluxIvar_z real ,
	modelFlux_u real ,
	modelFlux_g real ,
	modelFlux_r real ,
	modelFlux_i real ,
	modelFlux_z real ,
	modelFluxIvar_u real ,
	modelFluxIvar_g real ,
	modelFluxIvar_r real ,
	modelFluxIvar_i real ,
	modelFluxIvar_z real ,
	cModelFlux_u real ,
	cModelFlux_g real ,
	cModelFlux_r real ,
	cModelFlux_i real ,
	cModelFlux_z real ,
	cModelFluxIvar_u real ,
	cModelFluxIvar_g real ,
	cModelFluxIvar_r real ,
	cModelFluxIvar_i real ,
	cModelFluxIvar_z real ,
	aperFlux7_u real ,
	aperFlux7_g real ,
	aperFlux7_r real ,
	aperFlux7_i real ,
	aperFlux7_z real ,
	aperFlux7Ivar_u real ,
	aperFlux7Ivar_g real ,
	aperFlux7Ivar_r real ,
	aperFlux7Ivar_i real ,
	aperFlux7Ivar_z real ,
	lnLStar_u real ,
	lnLStar_g real ,
	lnLStar_r real ,
	lnLStar_i real ,
	lnLStar_z real ,
	lnLExp_u real ,
	lnLExp_g real ,
	lnLExp_r real ,
	lnLExp_i real ,
	lnLExp_z real ,
	lnLDeV_u real ,
	lnLDeV_g real ,
	lnLDeV_r real ,
	lnLDeV_i real ,
	lnLDeV_z real ,
	fracDeV_u real ,
	fracDeV_g real ,
	fracDeV_r real ,
	fracDeV_i real ,
	fracDeV_z real ,
	flags_u bigint ,
	flags_g bigint ,
	flags_r bigint ,
	flags_i bigint ,
	flags_z bigint ,
	type_u int ,
	type_g int ,
	type_r int ,
	type_i int ,
	type_z int ,
	probPSF_u real ,
	probPSF_g real ,
	probPSF_r real ,
	probPSF_i real ,
	probPSF_z real ,
	ra float ,
	dec float ,
	cx float ,
	cy float ,
	cz float ,
	raErr float ,
	decErr float ,
	b float ,
	l float ,
	offsetRa_u real ,
	offsetRa_g real ,
	offsetRa_r real ,
	offsetRa_i real ,
	offsetRa_z real ,
	offsetDec_u real ,
	offsetDec_g real ,
	offsetDec_r real ,
	offsetDec_i real ,
	offsetDec_z real ,
	extinction_u real ,
	extinction_g real ,
	extinction_r real ,
	extinction_i real ,
	extinction_z real ,
	psffwhm_u real ,
	psffwhm_g real ,
	psffwhm_r real ,
	psffwhm_i real ,
	psffwhm_z real ,
	mjd int ,
	airmass_u real ,
	airmass_g real ,
	airmass_r real ,
	airmass_i real ,
	airmass_z real ,
	phioffset_u real ,
	phioffset_g real ,
	phioffset_r real ,
	phioffset_i real ,
	phioffset_z real ,
	nProf_u int ,
	nProf_g int ,
	nProf_r int ,
	nProf_i int ,
	nProf_z int ,
	loadVersion int ,
	htmID bigint ,
	fieldID bigint ,
	parentID bigint ,
	specObjID bigint ,
	u real ,
	g real ,
	r real ,
	i real ,
	z real ,
	err_u real ,
	err_g real ,
	err_r real ,
	err_i real ,
	err_z real ,
	dered_u real ,
	dered_g real ,
	dered_r real ,
	dered_i real ,
	dered_z real ,
	cloudCam_u int ,
	cloudCam_g int ,
	cloudCam_r int ,
	cloudCam_i int ,
	cloudCam_z int ,
	resolveStatus int ,
	thingId int ,
	balkanId int ,
	nObserve int ,
	nDetect int ,
	nEdge int ,
	score real ,
	calibStatus_u int ,
	calibStatus_g int ,
	calibStatus_r int ,
	calibStatus_i int ,
	calibStatus_z int ,
	nMgyPerCount_u real ,
	nMgyPerCount_g real ,
	nMgyPerCount_r real ,
	nMgyPerCount_i real ,
	nMgyPerCount_z real ,
	TAI_u float ,
	TAI_g float ,
	TAI_r float ,
	TAI_i float ,
	TAI_z float 
)
location(
'gpfdist://192.168.100.78:8082/1G/PhotoObjAll1_comma.csv'
)
FORMAT 'CSV' ( DELIMITER ',' null as '');
--encoding 'UTF-8' LOG ERRORS INTO err_customer SEGMENT REJECT LIMIT 5;

