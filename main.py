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
    Specialitate(1, 'Drept civil', 'Dreptul civil este acea ramură de drept ce reglementează relațiile social-patrimoniale și nepatrimoniale stabilite între persoane fizice și/sau juridice ce se află pe poziții de egalitate juridică, chiar când una dintre părți este statul (ca persoană privată și nu ca autoritate publică). Echipa noastră acordă Consultanţă juridică, Asistenţă şi/sau Reprezentare într-o serie vastă de operațiuni specifice, ca de exemplu: Apărarea dreptului de proprietate privată; În materie de carte funciară; Acțiuni posesorii; În materie de succesiuni; Ieșiri din indiviziune (Partaj); În materie de răspundere civilă contractuală și delictuală; Transimisiune Creanţe (Cesiune de creanță, Preluare de datorie); Transformarea obligaţiiloe (Novația); Redactare, modificare și negociere a diferitelor contracte speciale; Acțiuni în nulitatea actelor; Acțiuni în constatare; Acțiuni privind dobândirea dreptului de proprietate prin uzucapiune și accesiune; Acțiuni în pretenții; Acțiuni posesorii; Procedura divorţului; Măsuri asigurătorii și provizorii; Cereri de valoare redusă; Procedura Ordonanței de plată; Procedura ordonanței președințiale; Acţiuni în evacuare; Plângeri contravenționale; Procedura recunoașterii hotărârilor străine pe teritoriul României; Exproprieri; Executări silite; Contestații la executare; Tranzacții; Legalizarea hotărârilor judecătorești; Negocieri; Alte cereri.'),
    Specialitate(2, 'Drept imobiliar', 'Conceptul de drept imobiliar desemnează ansamblul operaţiunilor privitoare la naşterea, modificarea sau singerea unor raporturi juridice privitoare la unul sau mai multe imobile. Echipa noastră oferă Consultanţă juridică, Asistenţă şi/sau Reprezentarea clientilor atât în faza precontractuală (analiză Documentaţie Tehnică/ Proiect Tehnic, Negocieri, ş.a), cât şi pe parcursul încheierii şi executării contractelor. Cu titlu de exemplu, menţionăm că oferim servicii juridice în legatură cu: Operatiunile de Vânzare sau cumpărare a imobilelor/Donaţie; Analiza situatiei juridice a proprietatilor; Redactarea antecontractelor, contractelor de vânzare-cumpărare, de închiriere sau ipotecă şi asistarea în faţa notarului public la semnare; Obtinerea de documente sau informatii referitoare la proprietatea în cauză; Obtinerea documentaţiei cadastrale, a incheierii de intabulare, deschiderea şi/sau modificarea de rol fiscal; Orice alte formalităţi în legatură cu încheierea tranzactiilor; Orice aspect sau conflict născut din raporturi locative sau de urbanism şi disciplina în construcţii; Dreptul de proprietate şi orice alte drepturi reale; Drepturi succesorale; Rezolutiunea contractelor de vânzare – cumpărare.'),
    Specialitate(3, 'Dreptul muncii', 'Echipa noastră oferă Consultanţă juridică, Asistenţă şi/sau Reprezentarea în domeniul reglementării raporturilor individuale şi colective de muncă (dreptul muncii, litigii de muncă). Privitor la raporturile individuale de muncă: Încheierea contractului individual de muncă; Modificarea contractului individual de muncă; Suspendarea contractului individual de muncă; Încetarea contractului individual de muncă; Drepturile şi obligaţiile angajatului / angajatorului; Timpul de muncă; Timpul de odihnă; concediile; Salarizarea şi alte drepturi bănesti; Sănătatea şi securitatea muncii; Conflictele de muncă; Întocmirea documentatiei legale pentru reglementarea raporturilor de munca cu privire la: clauza de neconcurenţă, clauza de confidentialitate, clauza de formare profesională, delegare în ţară şi/sau străinătate, detaşare în ţară şi/sau străinatate. Privitor la contractul colectiv de muncă: Purtarea negocierilor colective în vederea incheierii contractului colectiv de muncă; Redactarea contractului colectiv de muncă, în conformitate cu normele legale în vigoare din domeniul dreptului muncii; Asistenţă juridică în vederea semnării contractului colectiv de muncă; Reprezentarea societăţii comerciale în faţa autoritatilor (Inspectoratului Teritorial de Muncă / Direcţia de Muncă, Solidaritate Socială şi Familiei) în vederea înregistrarii contractului colectiv de munca. Servicii de consultanţă privind întocmirea Regulamentului de ordine interioară al societatii: Redactarea regulamentului de ordine interioară, în conformitate cu normele legale in vigoare din domeniul dreptului muncii si specificul de activitate al societăţii; Redactarea fişei postului, conţinȃnd principalele atribuţii, sarcini şi responsabilităţi ale salariaţilor. Servicii de consultanţă în vederea stabilirii unor relaţii de munca cu cetatenii straini in Romania: Obţinerea certificatului de rezidenţă temporară sau permanentă pentru cetatenii straini; Obţinerea numărului de în registrare fiscală în Romȃnia pentru cetăţenii străini; Obţinerea autorizaţiilor de muncă pentru angajarea cetăţenilor străini din afara UE; Recunosterea diplomelor de studiu pentru cetăţenii străini. Asistarea/Reprezentarea în instanţă cu privire la: Contestarea deciziilor de concediere / concediere abuzivă; Contestarea deciziilor de sancţionare disciplinară (sanctiuni disciplinare nefondate); Actionare în instanţă a angajatorului  pentru daune morale; Neplata drepturilor salariale.'),
    Specialitate(4, 'Drept penal', 'Echipa noastră poate acorda Consultanţă juridică, Asistenţă şi/sau Reprezentare persoanelor fizice /persoanelor juridice (şi a reprezentantilor acestora), în faţa organelor judiciare, pe tot parcursul: Urmăririi penale (audierilor, confruntărilor, măsuri preventive, asigurătorii, a expertizelor, încheierii unui acord de recunoaştere a vinovăţiei, ş.a); Camarei preliminare; Judecăţii (Fond/Apel/Căi extraordinare de atac); În procedurile procesuale ulterioare (Liberare condiţionată, Contestaţii la executare, Contopiri, Recunoaştere hotărâri judecătoreşti străine, Reabilitare, ş.a). Eforturile noastre se materializează prin elaborarea de apărări şi strategii complexe, redactarea de cereri, memorii, plângeri precum şi orice alte documente necesare. De asemenea, oferim asistenţă şi reprezentare în domeniul Dreptului penal al afacerilor, persoanelor fizice si juridice cercetate pentru săvarşirea de infractiuni la Legea societăţilor comerciale, a pietei de capital şi a altor legi cu incidenţă în domeniul comercial. Asistenţa în domeniul dreptului penal al afacerilor se realizeaza şi prin activitatea de prevenţie, prin oferirea de consultanţă (opinii juridice) şi redactarea de memorandumuri înainte de derularea unor operaţiuni comerciale.')]


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
