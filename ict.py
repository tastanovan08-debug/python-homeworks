import logging
from groq import Groq
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters, ContextTypes
)

# ═══════════════════════════════════════════════
#  БАПТАУЛАР (Settings)
# ═══════════════════════════════════════════════
TELEGRAM_TOKEN = " "
GROQ_API_KEY = ""  # Groq кілтін осы жерге қойыңыз

# Groq клиентін баптау
client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# 2025 жылғы көрсеткіштер
MZP = 85_000
AEK = 3_932


# ═══════════════════════════════════════════════
#  AI-МЕН БАЙЛАНЫС ФУНКЦИЯСЫ
# ═══════════════════════════════════════════════
def get_ai_response(user_text, system_instruction):
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Groq Error: {e}")
        return "❌ Кешіріңіз, AI сұранысты өңдей алмады."


# ═══════════════════════════════════════════════
#  КОМАНДАЛАР
# ═══════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧮 Калькулятор", callback_data="menu_calc"),
         InlineKeyboardButton("📋 Салық түрлері", callback_data="menu_types")],
        [InlineKeyboardButton("📅 Мерзімдер", callback_data="menu_deadlines"),
         InlineKeyboardButton("❓ Жиі сұрақтар", callback_data="menu_faq")],
        [InlineKeyboardButton("🚨 Алаяқтықты тексеру", callback_data="menu_scam")],
        [InlineKeyboardButton("📞 Байланыс", callback_data="menu_contacts")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🇰🇿 *Қазақстан Салық Боты (Groq AI)*\n\nСәлем! Мен салық және қаржы мәселелері бойынша көмекшіңмін.\n"
        "Төмендегі мәзірді қолданыңыз немесе сұрағыңызды тікелей жазыңыз 👇",
        parse_mode="Markdown", reply_markup=reply_markup
    )


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("📌 Қолдану: `/calc 300000`", parse_mode="Markdown")
        return
    try:
        salary = float(context.args[0].replace(" ", ""))
        jzq = salary * 0.10
        mjms = salary * 0.02
        tax_base = max(0, salary - jzq - mjms - 14 * AEK)
        jts = tax_base * 0.10
        net = salary - jzq - mjms - jts

        res = (f"💼 *Жалақы есебі (2025)*\n\n📥 Жалақы: {salary:,.0f} ₸\n"
               f"🔻 ЖЗҚ (10%): -{jzq:,.0f} ₸\n🔻 МЖМС (2%): -{mjms:,.0f} ₸\n"
               f"🔻 ЖТС (10%): -{jts:,.0f} ₸\n━━━━━━━━━━━━━━━\n"
               f"✅ Қолға алатыны: *{net:,.0f} ₸*")
        await update.message.reply_text(res, parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ Тек сан енгізіңіз.")


async def scam_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args) if context.args else ""
    if not user_text and update.message.reply_to_message:
        user_text = update.message.reply_to_message.text

    if not user_text:
        await update.message.reply_text(
            "🔍 *Алаяқтықты тексеру*\n\nМәтінді командадан кейін жазыңыз немесе хабарламаға 'reply' жасаңыз.")
        return

    await update.message.chat.send_action("typing")
    system_ins = "Сен Қазақстанның киберқауіпсіздік маманысың. Мәтінді талдап, оның алаяқтық екенін анықта. Қазақша жауап бер."
    prompt = f"Мына хабарлама алаяқтық па? Белгілерін атап көрсет: {user_text}"

    ai_reply = get_ai_response(prompt, system_ins)
    await update.message.reply_text(f"🚨 *AI Талдауы:*\n\n{ai_reply}", parse_mode="Markdown")


# ═══════════════════════════════════════════════
#  ӨҢДЕУШІЛЕР
# ═══════════════════════════════════════════════

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu_calc":
        await query.message.reply_text("🧮 Жалақы есептеу үшін `/calc 250000` деп жазыңыз.")
    elif query.data == "menu_types":
        await query.message.reply_text("📊 ЖТС: 10%, ҚҚС: 12%, КТС: 20%, Дивиденд: 5%.")
    elif query.data == "menu_deadlines":
        await query.message.reply_text(
            "📅 Салық төлеу: ай сайынғы 25-і. Декларация (250.00, 270.00): 15 қыркүйекке дейін.")
    elif query.data == "menu_scam":
        await query.message.reply_text("🚨 Күдікті мәтінді жіберіңіз немесе `/scam мәтін` деп жазыңыз.")
    elif query.data == "menu_contacts":
        contact_text = (
            "📞 *Салық органдарымен байланыс*\n\n"
            "🏛️ *КГД МҚМ (Қазақстан)*\n"
            "    ☎️ Колл-центр: 1414\n"
            "    🌐 cabinet.salyk.kz\n"
            "    📧 info@kgd.gov.kz\n\n"
            "🏙️ *Алматы қалалық салық департаменті*\n"
            "    📍 Алматы қ., Жибек жолы д-лы, 71\n"
            "    ☎️ +7 (727) 259-05-80\n\n"
            "⏰ *Жұмыс уақыты:* Дүйсенбі–Жұма, 09:00–18:30"
        )
        await query.message.reply_text(contact_text, parse_mode="Markdown")
    elif query.data == "menu_faq":
        await query.message.reply_text("❓ Сұрағыңызды тікелей жаза беріңіз, мен AI арқылы жауап беремін.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Егер хабарлама бағытталған (forward) болса, скам-тексеруді қосу
    if update.message.forward_date:
        context.args = [update.message.text]
        await scam_check(update, context)
        return

    await update.message.chat.send_action("typing")
    system_ins = "Сен Қазақстанның салық маманысың. Қазақ тілінде нақты әрі ресми жауап бер."
    ai_reply = get_ai_response(update.message.text, system_ins)
    await update.message.reply_text(ai_reply, parse_mode="Markdown")


# ═══════════════════════════════════════════════
#  ІСКЕ ҚОСУ
# ═══════════════════════════════════════════════

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Командалар
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calc))
    app.add_handler(CommandHandler("scam", scam_check))

    # Батырмалар
    app.add_handler(CallbackQueryHandler(button_handler))

    # Мәтіндік хабарламалар (AI)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Бот Groq AI негізінде іске қосылды...")
    app.run_polling()


if __name__ == "__main__":
    main()