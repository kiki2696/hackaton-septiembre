from modelos import db, Universidad, Parada, Horario, Bus
from flask import Flask 


# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "escuelas"

db.init_app(app)

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()

# Cargamos los datos en la base de datos
with app.app_context():

    ### cargar ciudades ###
    universidad_1 = Universidad(universidad='UCA')
    universidad_2 = Universidad(universidad='UNE')

    ### cargar paradas de bus ###
    # paradas de bus de her a uca
    parada_1_her_uca = Parada(parada='Puerta del Sol', latitud='', longitud='', ciudad='HER' , universidad_id=1)
    parada_2_her_uca = Parada(parada='Terminal Hernandarias', latitud='', longitud='', ciudad='HER' , universidad_id=1)
    parada_3_her_uca = Parada(parada='UCA', latitud='', longitud='', ciudad='HER' , universidad_id=1)
    # paradas de bus de cde a uca
    parada_1_cde_uca = Parada(parada='UCA', latitud='', longitud='', ciudad='CDE' , universidad_id=1)
    parada_2_cde_uca = Parada(parada='Estacion de Servicio Petrobras - Cavalcanti', latitud='', longitud='', ciudad='CDE' , universidad_id=1)
    parada_3_cde_uca = Parada(parada='Rotonda - Area 1', latitud='', longitud='', ciudad='CDE' , universidad_id=1)
    # paradas de bus de cde a une
    parada_1_cde_une = Parada(parada='Terminal CDE', latitud='', longitud='', ciudad='CDE' , universidad_id=2)
    parada_2_cde_une = Parada(parada='Estacion de Servicio Petrobras - KM7', latitud='', longitud='', ciudad='CDE' , universidad_id=2)
    parada_3_cde_une = Parada(parada='UNE', latitud='', longitud='', ciudad='CDE' , universidad_id=2)
    # paradas de bus de her a une
    parada_1_her_une = Parada(parada='UNE', latitud='', longitud='', ciudad='HER' , universidad_id=2)
    parada_2_her_une = Parada(parada='Colegio Nacional Soldado Paraguayo - Don Bosco', latitud='', longitud='', ciudad='HER' , universidad_id=2)
    parada_3_her_une = Parada(parada='Rotonda - Area 6', latitud='', longitud='', ciudad='HER' , universidad_id=2)
    # parada horario final
    parada_final = Parada(parada='horario', latitud='', longitud='', ciudad='nulo' , universidad_id=1)

    ### cargar horarios ###
    ## turno manhana
    # para las 7:00 her
    horario_1_her_puerta_sol = Horario(turno='manhana', horario='6:20', parada=parada_1_her_uca)
    horario_1_her_terminal_her = Horario(turno='manhana', horario='6:35', parada=parada_2_her_uca)
    horario_1_her_uca1 = Horario(turno='manhana', horario='7:00', parada=parada_3_her_uca)
     # para las 7:00 cde
    horario_1_her_terminal_cde = Horario(turno='manhana', horario='6:20', parada=parada_1_cde_uca)
    horario_1_her_km4 = Horario(turno='manhana', horario='6:35', parada=parada_2_cde_uca)
    horario_1_her_uca2 = Horario(turno='manhana', horario='7:00', parada=parada_3_cde_uca)
    ## turno tarde 
    # para las 2:00 her
    horario_2_her_puerta_sol = Horario(turno='tarde', horario='13:20', parada=parada_1_her_uca)
    horario_2_her_terminal_her = Horario(turno='tarde', horario='13:35', parada=parada_2_her_uca)
    horario_2_her_uca1 = Horario(turno='tarde', horario='14:00', parada=parada_3_her_uca)
    # para las 2:00 cde
    horario_2_her_terminal_cde = Horario(turno='tarde', horario='13:20', parada=parada_1_her_uca)
    horario_2_her_km4 = Horario(turno='tarde', horario='13:35', parada=parada_2_cde_uca)
    horario_2_her_uca2 = Horario(turno='tarde', horario='14:00', parada=parada_3_her_uca)
    ## turno noche
    # para las 10:30 her
    horario_3_her_puerta_sol = Horario(turno='noche', horario='9:50', parada=parada_1_her_uca)
    horario_3_her_terminal_her = Horario(turno='noche', horario='10:05', parada=parada_2_her_uca)
    horario_3_her_uca1 = Horario(turno='noche', horario='10:30', parada=parada_3_her_uca)
    # para las 10:30 cde
    horario_3_her_terminal_cde = Horario(turno='noche', horario='9:50', parada=parada_2_her_uca)
    horario_3_her_km4 = Horario(turno='noche', horario='10:05', parada=parada_1_cde_uca)
    horario_3_her_uca2 = Horario(turno='noche', horario='10:30', parada=parada_3_her_uca)


    # horario final
    # horario manhana
    horario_m1 = Horario(turno='manhana', horario='7:00', parada=parada_final)
    horario_m2 = Horario(turno='manhana', horario='10:00', parada=parada_final)

    # horario tarde
    horario_t1 = Horario(turno='tarde', horario='14:00', parada=parada_final)
    horario_t2 = Horario(turno='tarde', horario='17:00', parada=parada_final)

    # horario noche
    horario_n1 = Horario(turno='noche', horario='19:00', parada=parada_final)
    horario_n2 = Horario(turno='noche', horario='22:30', parada=parada_final)

    ### cargar buses ###
    # bus uca
    bus_uca_1 = Bus(bus='UCA 1', chapa='ZDO345', universidad_id=1, parada_id=4, horario_id=3)
    bus_uca_2 = Bus(bus='UCA 2', chapa='QWE123', universidad_id=1, parada_id=4, horario_id=3)
    # bus une
    bus_une_1 = Bus(bus='UNE 1', chapa='ASD456', universidad_id=2, parada_id=9, horario_id=3)
    bus_une_1 = Bus(bus='UNE 2', chapa='DFJ459', universidad_id=2, parada_id=9, horario_id=3)

    # agregar los datos a la base de datos
    db.session.add(universidad_1)
    db.session.add(universidad_2)
    db.session.add(parada_1_her_uca)
    db.session.add(parada_2_her_uca)
    db.session.add(parada_3_her_uca)
    db.session.add(parada_3_cde_uca)
    db.session.add(parada_2_cde_uca)
    db.session.add(parada_1_cde_uca)
    db.session.add(parada_1_cde_une)
    db.session.add(parada_2_cde_une)
    db.session.add(parada_3_cde_une)
    db.session.add(parada_3_her_une)
    db.session.add(parada_2_her_une)
    db.session.add(parada_1_her_une)
    db.session.add(parada_final)
    db.session.add(horario_1_her_puerta_sol)
    db.session.add(horario_1_her_terminal_her)
    db.session.add(horario_1_her_uca1)
    db.session.add(horario_1_her_terminal_cde)
    db.session.add(horario_1_her_km4)
    db.session.add(horario_1_her_uca2)
    db.session.add(horario_2_her_puerta_sol)
    db.session.add(horario_2_her_terminal_her)
    db.session.add(horario_2_her_uca1)
    db.session.add(horario_2_her_terminal_cde)
    db.session.add(horario_2_her_km4)
    db.session.add(horario_2_her_uca2)
    db.session.add(horario_3_her_puerta_sol)
    db.session.add(horario_3_her_terminal_her)
    db.session.add(horario_3_her_uca1)
    db.session.add(horario_3_her_terminal_cde)
    db.session.add(horario_3_her_km4)
    db.session.add(horario_3_her_uca2)
    db.session.add(bus_uca_1)
    db.session.add(bus_uca_2)
    db.session.add(bus_une_1)
    db.session.add(bus_une_1)
    db.session.commit()

