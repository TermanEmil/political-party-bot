from telegram import Update
from telegram.ext import ContextTypes


async def party_agenda_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = '\n\n'.join([
        '• MAN crede ferm în Republica Moldova, ca stat suveran, indivizibil, neutru și cu un potențial puternic '
            'de a deveni un membru demn al comunității europene.',
        '• MAN este un partid politic, care urmărește o agendă democratică în Republica Moldova. Credem '
            'în libertate, democrație, justiție socială, echitate, solidaritate, incluziune și sprijin pentru '
            'fiecare membru al societății.',
        '• MAN are un respect enorm pentru rădăcinile poporului țării, pentru cultura, tradițiile și '
            'identitatea noastră, acestea fiind valorile de bază pe care le împărtășim.',
        '• MAN crede cu tărie că puterea Republicii Moldovei constă în unitatea și diversitatea societății și că '
            'cetățenii noștri sunt cea mai valoroasă resursă pe termen lung pe care o avem. Suntem siguri că Moldova și '
            'oamenii ei vor fi, cu certitudine, în viitorul apropiat valoarea adăugată pentru întreaga comunitate europeană.'
            ' MAN împărtășește doctrina social-democrată de tip european.',
        '• MAN pledează pentru creșterea continuă a nivelului și a calității de trai a oamenilor, pentru transformarea '
            'Republicii Moldova într-un stat cu o mare clasă de mijloc bogată, care, după exemplul Comunității Europene, '
            'este baza unei societăţi de succes.',
        '• MAN va promova o abordare inovativă, vizionară și consecventă în implementarea politicilor de stat, în '
            'conformitate cu principiile social-democrate, care vor aduce bunăstare oamenilor.',
        '• MAN este partidul rezultatelor, a oamenilor competenți și profesioniști, care au demonstrat la nivel de '
            'Chișinău că pot schimba lucrurile în bine, în pofida celor mai dificile circumstanțe. Vom demonstra că se '
            'poate de făcut acest lucru și la nivel de țară.',
        '• MAN consideră că integrarea europeană a Republicii Moldova trebuie să devină idee națională. MAN va propune'
            ' semnarea unui pact similar celui de la Snagov.',
        '• MAN va depune toate eforturile ca, în cel mai scurt timp, Republica Moldova să devină membru plenipotențiar '
            'al Uniunii Europene.',
    ])

    await update.message.reply_text(text)
