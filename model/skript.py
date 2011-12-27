gamma_c = 5714.28		% zadani elektricke vodivosti medi
j_c = 6000			% zadani proudove hustoty medi
mu_c = 1			% zadani permeability medi
mu_a = 1			% zadani permeability vzduchu
mu_f = 1000			% zadani permeability zeleza
gamma_f = 2000			% zadani elektricke vodivosti zeleza

r_in = 1
a = 0.3
b = 1.8

a_fe = 2
b_fe = 3
c_fe =0.1
d_fe = 2

newdocument("rozlozeni_magnetickeho_pole_v_okoli_vzduchovych_tlumivek", "axisymmetric", "magnetic", 1, 2, "disabled", 1, 1, 50, "harmonic", 1, 1, 0)

addboundary("A=0", "magnetic_vector_potential", 0, 0)

addmaterial("cuprum", j_c, 0, mu_c, gamma_c, 0, 0, 0, 0, 0)
addmaterial("air", 0, 0, 1, 0, 0, 0, 0, 0, 0)
addmaterial("fe", 0, 0, mu_f, gamma_f, 0, 0, 0, 0, 0)


addedge(r_in , 0, r_in + a, 0, 0, "none")
addedge(r_in + a, 0, r_in + a, b, 0, "none")
addedge(r_in + a, b, r_in, b, 0, "none")
addedge(r_in, b , r_in, 0, 0, "none")

addedge(0, -10*b, 20*r_in, 0, 90, "A=0")
addedge( 20*r_in, 0, 0, 10*b, 90, "A=0")
addedge( 0, 10*b, 0, -10*b, 0, "A=0")

addedge(0 , b_fe, a_fe, d_fe, 0, "none")
addedge(a_fe, d_fe, a_fe , d_fe + c_fe, 0, "none")
addedge(a_fe , d_fe + c_fe, 0, b_fe+c_fe, 0, "none")
addedge(0, b_fe+c_fe, 0 , b_fe, 0, "none")


addlabel(a_fe/2, (b_fe+c_fe+d_fe)/2, 0, 0, "fe")
addlabel(r_in+a/2, b/2, 0, 0, "cuprum")
addlabel(r_in/2, b/2, 0, 0, "air")





newdocument("rozlozeni_magnetickeho_pole_v_okoli_vzduchovych_tlumivek_teplotni_pole", "axisymmetric", "heat", 1, 2, "disabled", 1, 1, 0, "transient", 1, 1, 0)

addboundary("temperature", "heat_temperature", 20)

addmaterial("cuprum", j_c, 0, mu_c, gamma_c, 0, 0, 0, 0, 0)
addmaterial("air", 0, 0, 1, 0, 0, 0, 0, 0, 0)
addmaterial("fe", 0, 0, mu_f, gamma_f, 0, 0, 0, 0, 0)

addedge(r_in , 0, r_in + a, 0, 0, "none")
addedge(r_in + a, 0, r_in + a, b, 0, "none")
addedge(r_in + a, b, r_in, b, 0, "none")
addedge(r_in, b , r_in, 0, 0, "none")

addedge(0, -10*b, 20*r_in, 0, 90, "temperature")
addedge( 20*r_in, 0, 0, 10*b, 90, "temperature")
addedge( 0, 10*b, 0, -10*b, 0, "temperature")

addedge(0 , b_fe, a_fe, d_fe, 0, "none")
addedge(a_fe, d_fe, a_fe , d_fe + c_fe, 0, "none")
addedge(a_fe , d_fe + c_fe, 0, b_fe+c_fe, 0, "none")
addedge(0, b_fe+c_fe, 0 , b_fe, 0, "none")


addlabel(a_fe/2, (b_fe+c_fe+d_fe)/2, 0, 0, "fe")
addlabel(r_in+a/2, b/2, 0, 0, "cuprum")
addlabel(r_in/2, b/2, 0, 0, "air")
