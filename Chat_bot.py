import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs and reflections
pairs = [
    [
        r"မင်္ဂလာပါ|Hi|Hello",
        ["မင်္ဂလာပါ Simbolo မှ ကြိုဆိုပါတယ်"],
    ],
    [
        r"သင်တန်း|အတန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["AI အတန်းရယ် Data Science အတန်းလေးရယ်ရှိပါတယ်"],
    ],
    [
        r"AI| Artificial Intelligence|အတန်း|သင်တန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["Artificial Intelligence အတန်းမှာဆို Python Programming ကနေ Applied NLP,Computer Vision အထိ အတန်း (၆) တန်းရှိပါတယ်"],
    ],
    [
        r"DS|Data Science|အတန်း|သင်တန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["Data Science အတန်းမှာဆို Python programming သင်တန်းကနေ Power BI အထိ အတန်း(၇)တန်းရှိပါတယ်"],
    ],
    [
        r"ကာလ|အချိန်|အချိန်ကာလ ဘယ်လောက်ကြာနိုင်လဲ| ဘယ်လောက်တတ်ရမလဲ|ဘယ်လောက်တတ်ရမလဲ",
        ["Pathway တစ်ခုစီ အပြီးထိတတ်မည်ဆိုပါက တစ်နှစ်ကြာနိုင်ပါတယ်။ Pathway များမှ သင်တန်းတစ်ခုစီဆိုရင် (၂) ခန့်ကြာမြင့်ပါမည်။"],
    ],
    [
        r"class|class ကြေး|Course|Course Fee|Fee|ဘယ်လောက်လဲ|သိပါရစေ|သိချင်ပါတယ်",
        ["သင်တန်းကြေးကတော့ မြန်မာငွေ - ၇၀,၀၀၀/-ကျပ်ကျသင့်ပါမည်ဖြစ်ပြီး Kpay၊ Wavepay ဖြင့် ပေးချေနိုင်ပါသည်။"],
    ],
    [
        r"သင်ကြားပုံ|class system|သင်ကြားရေးစနစ် က ဘယ်လိုလဲ|ဘယ်လိုသင်တာလဲ",
        ["သင်တန်:ရဲ့ သင်ကြားပုံက တစ်ပတ်ကို နှစ်ရက် zoom  မှ သင်ကြားပြီး Google Class မှာ record ပြန်တင်ပေးပြီး Assignment System ဖြစ်လို့ ပုံမှန် Assignment တင်ပေးပြီး Project တစ်ခုတင်ပေးရပါတယ်"],
    ],
    [
        r"Thank| ပြောပြလို့|ရှင်းပြပေးလို့ |ဖြေကြားပေးလို့|ကျေးဇူးပါ|ကျေးဇူး|နားလည်ပါပြီ",
        ["ဟုတ်ကဲ့စိတ်ဝင်စားလိုကျေးဇူးပါ။ အကယ်၍ သိချင်တာတစ်ခုရှိပါက မေးထားလို့ရပါတယ်။ Admin လာတဲ့အခါ ဖြေ‌ကြားပေးပါ့မယ်"],
    ],
      [
        r"Who|ဘယ်သူလဲ|မင်းကဘယ်သူလဲ|အခုဖြေတာမင်မင်လား|နာမည်လေးသိချင်ပါတယ်",
        ["ဟုတ်ကဲ့စိတ်ဝင်စားလိုကျေးဇူးပါ။ ငါက ကျွန်တော်/ကျွန်မ မဟုတ်တဲ့ Simbolo သင်တန်းသားတစ်ယောက် NLTK နဲ့ ရေးသားထားလူလုပ်မှတ်ဉာဏ်တစ်ခုသာဖြစ်ပါတယ်"],
    ],

]

# Define pronouns
reflections = {
    "ကျွန်တော်": "အကိုရေ",
    "ကျွန်မ": "အမရေ",
    # Add more reflections as needed
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

def burmese_chatbot():
    st.title("Burmese Chatbot with Streamlit")
    st.write("မင်္ဂလာပါ! Simbolo သင်တန်းမှ ဆိုကြိုပါတယ်။ 'bye' လို့ရိုက်ပါက ပြီးဆုံးပါမည်")

    user_input = st.text_input("You:")
    
    if user_input:
        if user_input.lower() == "bye":
            st.write("Chatbot: Goodbye!")
        else:
            response = chatbot.respond(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    burmese_chatbot()
