from telegram import Update
from telegram.ext import ContextTypes


async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = '\n'.join([
        'Principiul de bază care a stat, stă și va sta la constituirea Partidului '
        'Mișcarea Alternativă Națională (MAN) este interesul statului și al '
        'cetățenilor. Am demonstrat că putem dezvolta Chișinăul și suntem siguri '
        'că vom reuși și la nivel de țară. Oamenii din echipă și cei care vor adera în '
        'continuare sunt specialiști, care își cunosc munca și care pot face față '
        'indiferent de situații de crize și risc. Avem un potențial enorm atât în țară, '
        'cât și pe plan extern, să devenim un pol atractiv de dezvoltare.'
    ])

    await update.message.reply_photo('./resources/party-photo.jpg', caption=text)
