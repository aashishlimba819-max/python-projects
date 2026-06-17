import requests

currency=("USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG",
"AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB",
"BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF",
"CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK",
"DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP",
"GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
"HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK",
"JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD",
"KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL",
"MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN",
"MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB",
"PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB",
"RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL",
"SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND",
"TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "UYU", "UZS",
"VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF", "XPF",
"YER", "ZAR", "ZMW", "ZWG", "ZWL")

  #India Rupee INR ₹ ,USA Dollar USD $
                #Europe Euro EUR €
                #Japan Yen JPY ¥
                #UK Pound GBP £
                #Canada Dollar CAD $
                #Australia Dollar AUD $

ask1=input("Enter the source currency(INR/USD/GBP/EUR/JPY/CNY/CAD/AUD)").upper()
amount=int(input("Enter the amount :"))
list=[]
list1=[]
how_many=int(input("How many currency you want to convert ?"))
i=1
API_KEY="fb93cc7fd05ccc21b185edd2"
url=f"https://v6.exchangerate-api.com/v6/fb93cc7fd05ccc21b185edd2/latest/{ask1}"
response = requests.get(url)
data=response.json()

while i<=how_many:
    which_currency=input("Enter the target currency(INR/USD/GBP/EUR/JPY/CNY/CAD/AUD)").upper()
# date= 6/17/2026    
#     rates = {
#     "INR": 94.47,
#     "EUR": 0.86,
#     "JPY": 160.29,
#     "CNY": 6.76,
#     "GBP": 0.75,
#     "CAD": 1.4,
#     "AUD": 1.42,
#     "USD":1
# }
    if(ask1 and which_currency not in currency):
        print("Invalid choice")
        break
    if(ask1 and which_currency in currency):    
        value=((data["conversion_rates"][which_currency]*amount)/data["conversion_rates"][ask1])
        list.append(value)
        list1.append(which_currency)
        i+=1  
if(ask1 and which_currency in currency):
    j=0
    while j<len(list1):
        print(amount,ask1,"is equal to",list[j],list1[j])
        j+=1
print("Thank you!!")





    
