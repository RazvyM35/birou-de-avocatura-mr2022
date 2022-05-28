from flask import Flask, render_template, request


app = Flask('Birou de avoocatura MR')


@app.route('/')
@app.route('/acasa/')
def show_acasa():
    pagina = 'acasa'
    return render_template('acasa.html',
                           pagina=pagina)


class Specialitate:
    def __init__(self, idspec, numespec, descriere):
        self.idspec = idspec
        self.numespec = numespec
        self.descriere = descriere


# creating list
specialitati = [
    Specialitate(1, 'Drept civil', 'Dreptul civil este acea ramură de drept ce reglementează relațiile'
                                   ' social-patrimoniale și nepatrimoniale stabilite între persoane fizice și/sau juridice'
                                   ' ce se află pe poziții de egalitate juridică, chiar când una dintre părți este statul '
                                   '(ca persoană privată și nu ca autoritate publică).'),
    Specialitate(2, 'Drept imobiliar', 'Conceptul de drept imobiliar desemnează ansamblul operaţiunilor privitoare la naşterea,'
                                       ' modificarea sau singerea unor raporturi juridice privitoare la unul sau mai multe imobile.'),
    Specialitate(3, 'Dreptul muncii', 'Echipa noastră oferă Consultanţă juridică, Asistenţă şi/sau Reprezentarea în domeniul '
                                      'reglementării raporturilor individuale şi colective de muncă (dreptul muncii, litigii de muncă).'),
    Specialitate(4, 'Drept penal', 'Echipa noastră poate acorda Consultanţă juridică, Asistenţă şi/sau Reprezentare persoanelor '
                                   'fizice /persoanelor juridice (şi a reprezentantilor acestora), în faţa organelor judiciare, pe tot parcursul. ' 
                                   'Eforturile noastre se materializează prin elaborarea de apărări şi strategii complexe, redactarea de cereri,'
                                   ' memorii, plângeri precum şi orice alte documente necesare.')]


class Avocat:
    def __init__(self, id, nume, prenume, idspec, numespec):
        self.id = id
        self.nume = nume
        self.prenume = prenume
        self.idspec = idspec
        self.numespec = numespec


# creating list
avocati = [
    Avocat(1, 'Gheorghe', 'Dinca', 1, 'Drept civil'),
    Avocat(2, 'Andreea', 'Florea', 2, 'Drept imobiliar'),
    Avocat(3, 'Floretin', 'Cristi', 3, 'Dreptul muncii'),
    Avocat(4, 'Viorel', 'Ionescu', 4, 'Drept penal'),
    Avocat(5, 'Ion', 'Popescu', 4, 'Drept penal'),
    Avocat(6, 'Mihai', 'Vasilescu', 4, 'Drept penal')]


@app.route('/avocati/')
def show_avocati():
    pagina = 'avocati'
    return render_template('avocati.html',
                           title='Echipa de avocati',
                           avocati=avocati,
                           pagina=pagina)


@app.route('/avocat/<int:id>/')
def show_avocat(id):
    pagina = 'avocat'
    avocat = next((avocat for avocat in avocati if avocat.id == id), None)
    if avocat:
        title = f'{avocat.nume} {avocat.prenume}'
    else:
        title = 'Avocat inexistent'
    return render_template('avocat.html',
                           title=title,
                           avocat=avocat,
                           pagina=pagina)


@app.route('/cauta/', methods=['GET', 'POST'])
def cauta_avocat():
    pagina = 'cauta'
    if request.method == 'POST':
        argumentCautare = request.form
    else:
        argumentCautare = request.args

    cauta = argumentCautare.get('cauta').strip().lower()

    rezultatCautare = [avocat for avocat in avocati if cauta in avocat.nume.lower() or cauta in avocat.prenume.lower()]

    return render_template('avocati.html',
                           title='Echipa de avocati',
                           avocati=rezultatCautare,
                           search=cauta,
                           pagina=pagina)


@app.route('/specialitati/')
def show_specialitati():
    pagina = 'specialitati'
    return render_template('specialitati.html',
                           specialitati=specialitati,
                           pagina=pagina)


@app.route('/specialitate/<int:idspec>/')
def show_specialitate(idspec):
    pagina = 'specialitate'
    rezultatCautare = [avocat for avocat in avocati if avocat.idspec == idspec]
    specialitate = next((spec for spec in specialitati if spec.idspec == idspec), None)
    if specialitate:
        descriere = specialitate.descriere
        numespec = specialitate.numespec
        title = 'Ramura ' + (specialitate.numespec or '')
    else:
        descriere = ''
        numespec = ''
        title = 'Ramura inexistenta'
    return render_template('specialitate.html',
                           avocati=rezultatCautare,
                           numespec=numespec,
                           title=title,
                           pagina=pagina,
                           descriere=descriere)


@app.route('/contact/')
def contact():
    pagina = 'contact'
    return render_template('contact.html',
                           title='Contact',
                           pagina=pagina)


@app.errorhandler(404)
def page_not_found(e):
    """Catch in-existent routes"""
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
