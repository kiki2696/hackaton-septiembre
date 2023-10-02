from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Universidad, Parada, Horario, Bus

# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "escuelas"


# Inicializar la base de datos
db.init_app(app)

### RUTAS ###
# ruta principal - landing page
@app.route('/')
def index():
    return render_template('index.html')

# ruta home - homepage - mapas
@app.route('/home')
def home():
    return render_template('mapa.html')

# ruta ciudad - escoger una ciudad
@app.route('/universidad')
def universidad():
    universidades = Universidad.query.all()
    return render_template('universidad.html', universidades=universidades)

# ruta parada - escoger una parada
@app.route('/parada/<id>')
def parada(id):
    paradas = Parada.query.filter_by(universidad_id=id).all()
    universidad = Universidad.query.get(id)

    # Separar las paradas en las categorías "HERNANDARIAS A UCA" y "CDE A UCA"
    parada_uca_her = [parada for parada in paradas if parada.ciudad == 'HER']
    parada_uca_cde = [parada for parada in paradas if parada.ciudad == 'CDE']

    return render_template('paradas.html', paradas=paradas, parada_uca_her=parada_uca_her, parada_uca_cde=parada_uca_cde, universidad=universidad)

# ruta horario - escoger un horario
@app.route('/horario')
def horario():
    
    parada_final = Parada.query.filter_by(parada='horario').first()

    # Filtrar los horarios para la parada específica y turno de la mañana
    turno_manhana = Horario.query.filter_by(turno='manhana', parada=parada_final).all()
    
    # Filtrar los horarios para la parada específica y turno de la tarde
    turno_tarde = Horario.query.filter_by(turno='tarde', parada=parada_final).all()

    # Filtrar los horarios para la parada específica y turno de la noche
    turno_noche = Horario.query.filter_by(turno='noche', parada=parada_final).all()

    return render_template('horario.html', turno_manhana=turno_manhana, turno_tarde=turno_tarde, turno_noche=turno_noche)







### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)
