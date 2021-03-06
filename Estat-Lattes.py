
import urllib.request
import os
import zipfile
import csv
import lxml
import unidecode
import pygal
import pygal_maps_world
import datetime

# dicionario de países para permitir a exibicao por extenso nos graficos
paises_3digitos = {}
paises_3digitos["AFG"] = "Afeganistão"
paises_3digitos["ZAF"] = "África do Sul"
paises_3digitos["ALB"] = "Albânia"
paises_3digitos["DEU"] = "Alemanha"
paises_3digitos["AND"] = "Andorra"
paises_3digitos["AGO"] = "Angola"
paises_3digitos["AIA"] = "Anguila"
paises_3digitos["ATA"] = "Antártida"
paises_3digitos["ATG"] = "Antigua e Barbuda"
paises_3digitos["ANT"] = "Antilhas Holandesas"
paises_3digitos["SAU"] = "Arábia Saudita"
paises_3digitos["DZA"] = "Argélia"
paises_3digitos["ARG"] = "Argentina"
paises_3digitos["ARM"] = "Arménia"
paises_3digitos["ABW"] = "Aruba"
paises_3digitos["AUS"] = "Austrália"
paises_3digitos["AUT"] = "Áustria"
paises_3digitos["AZE"] = "Azerbaijão"
paises_3digitos["BHS"] = "Bahamas"
paises_3digitos["BHR"] = "Bahrein"
paises_3digitos["BGD"] = "Bangladesh"
paises_3digitos["BRB"] = "Barbados"
paises_3digitos["BEL"] = "Bélgica"
paises_3digitos["BLZ"] = "Belize"
paises_3digitos["BEN"] = "Benim"
paises_3digitos["BMU"] = "Bermudas"
paises_3digitos["BLR"] = "Bielorrússia"
paises_3digitos["BOL"] = "Bolívia"
paises_3digitos["BES"] = "Bonaire, San Eustaquio y Saba"
paises_3digitos["BIH"] = "Bósnia-Herzegovina"
paises_3digitos["BWA"] = "Botsuana"
paises_3digitos["BRA"] = "Brasil"
paises_3digitos["BRN"] = "Brunei"
paises_3digitos["BGR"] = "Bulgária"
paises_3digitos["BFA"] = "Burkina Fasso"
paises_3digitos["BDI"] = "Burundi"
paises_3digitos["BTN"] = "Butão"
paises_3digitos["CPV"] = "Cabo Verde"
paises_3digitos["CMR"] = "Camarões"
paises_3digitos["KHM"] = "Camboja"
paises_3digitos["CAN"] = "Canadá"
paises_3digitos["KAZ"] = "Cazaquistão"
paises_3digitos["TCD"] = "Chade"
paises_3digitos["CHL"] = "Chile"
paises_3digitos["CHN"] = "China"
paises_3digitos["CYP"] = "Chipre"
paises_3digitos["COL"] = "Colômbia"
paises_3digitos["COM"] = "Comoras"
paises_3digitos["COG"] = "Congo"
paises_3digitos["PRK"] = "Coreia do Norte"
paises_3digitos["KOR"] = "Coreia do Sul"
paises_3digitos["CIV"] = "Costa do Marfim"
paises_3digitos["CRI"] = "Costa Rica"
paises_3digitos["HRV"] = "Croácia"
paises_3digitos["CUB"] = "Cuba"
paises_3digitos["CUW"] = "Curazao"
paises_3digitos["DNK"] = "Dinamarca"
paises_3digitos["DJI"] = "Djibouti"
paises_3digitos["DMA"] = "Dominica"
paises_3digitos["EGY"] = "Egito"
paises_3digitos["SLV"] = "El Salvador"
paises_3digitos["ARE"] = "Emirados Árabes Unidos"
paises_3digitos["ECU"] = "Equador"
paises_3digitos["ERI"] = "Eritreia"
paises_3digitos["SVK"] = "Eslováquia"
paises_3digitos["SVN"] = "Eslovênia"
paises_3digitos["ESP"] = "Espanha"
paises_3digitos["USA"] = "Estados Unidos"
paises_3digitos["EST"] = "Estônia"
paises_3digitos["ETH"] = "Etiópia"
paises_3digitos["FJI"] = "Fiji"
paises_3digitos["PHL"] = "Flipinas"
paises_3digitos["FIN"] = "Finlândia"
paises_3digitos["FRA"] = "França"
paises_3digitos["GAB"] = "Gabão"
paises_3digitos["GMB"] = "Gâmbia"
paises_3digitos["GHA"] = "Gana"
paises_3digitos["GEO"] = "Geórgia"
paises_3digitos["GIB"] = "Gibraltar"
paises_3digitos["GBR"] = "Grã-Bretanha"
paises_3digitos["GRD"] = "Granada"
paises_3digitos["GRC"] = "Grécia"
paises_3digitos["GRL"] = "Gronelândia"
paises_3digitos["GLP"] = "Guadalupe"
paises_3digitos["GUM"] = "Guam"
paises_3digitos["GTM"] = "Guatemala"
paises_3digitos["GGY"] = "Guernsey"
paises_3digitos["GUY"] = "Guiana"
paises_3digitos["GUF"] = "Guiana Francesa"
paises_3digitos["GIN"] = "Guiné"
paises_3digitos["GNQ"] = "Guinea Ecuatorial"
paises_3digitos["GNQ"] = "Guiné Equatorial"
paises_3digitos["GNB"] = "Guiné-Bissau"
paises_3digitos["HTI"] = "Haiti"
paises_3digitos["NLD"] = "Holanda"
paises_3digitos["HND"] = "Honduras"
paises_3digitos["HKG"] = "Hong Kong"
paises_3digitos["HUN"] = "Hungria"
paises_3digitos["YEM"] = "Iémen"
paises_3digitos["BVT"] = "Ilhas Bouvet"
paises_3digitos["IMN"] = "Ilha de Man"
paises_3digitos["CXR"] = "Ilha do Natal"
paises_3digitos["PCN"] = "Ilha Pitcairn"
paises_3digitos["REU"] = "Ilha Reunião"
paises_3digitos["ALA"] = "Ilhas Aland"
paises_3digitos["CYM"] = "Ilhas Cayman"
paises_3digitos["CCK"] = "Ilhas Cocos"
paises_3digitos["COM"] = "Ilhas Comores"
paises_3digitos["COK"] = "Ilhas Cook"
paises_3digitos["FRO"] = "Ilhas Faroé"
paises_3digitos["SGS"] = "Ilhas Geórgia do Sul e Sandwich do Sul"
paises_3digitos["HMD"] = "Ilhas Heard e McDonald"
paises_3digitos["MNP"] = "Ilhas Marianas do Norte"
paises_3digitos["MHL"] = "Ilhas Marshall"
paises_3digitos["FLK"] = "Ilhas Malvinas"
paises_3digitos["UMI"] = "Ilhas Menores dos Estados Unidos"
paises_3digitos["NFK"] = "Ilhas Norfolk"
paises_3digitos["CXR"] = "Ilha de Páscoa"
paises_3digitos["SYC"] = "Ilhas Seychelles"
paises_3digitos["SLB"] = "Ilhas Salomão"
paises_3digitos["SJM"] = "Ilhas Svalbard e Jan Mayen"
paises_3digitos["TKL"] = "Ilhas Tokelau"
paises_3digitos["TCA"] = "Ilhas Turks e Caicos"
paises_3digitos["VIR"] = "Ilhas Virgens (EUA)"
paises_3digitos["VGB"] = "Ilhas Vírgens Britânicas"
paises_3digitos["WLF"] = "Ilhas Wallis e Futuna"
paises_3digitos["IND"] = "Índia"
paises_3digitos["IDN"] = "Indonésia"
paises_3digitos["IRN"] = "Irão"
paises_3digitos["IRQ"] = "Iraque"
paises_3digitos["IRL"] = "Irlanda"
paises_3digitos["ISL"] = "Islândia"
paises_3digitos["ISR"] = "Israel"
paises_3digitos["ITA"] = "Itália"
paises_3digitos["JAM"] = "Jamaica"
paises_3digitos["JPN"] = "Japão"
paises_3digitos["JEY"] = "Jersey"
paises_3digitos["JOR"] = "Jordânia"
paises_3digitos["KIR"] = "Kiribati"
paises_3digitos["KWT"] = "Kuwait"
paises_3digitos["LAO"] = "Laos"
paises_3digitos["LVA"] = "Letônia"
paises_3digitos["LSO"] = "Lesoto"
paises_3digitos["LBN"] = "Líbano"
paises_3digitos["LBR"] = "Libéria"
paises_3digitos["LBY"] = "Líbia"
paises_3digitos["LIE"] = "Liechtenstein"
paises_3digitos["LTU"] = "Lituânia"
paises_3digitos["LUX"] = "Luxemburgo"
paises_3digitos["MAC"] = "Macau"
paises_3digitos["MKD"] = "Macedônia"
paises_3digitos["MDG"] = "Madagascar"
paises_3digitos["MYS"] = "Malásia"
paises_3digitos["MWI"] = "Malaui"
paises_3digitos["MDV"] = "Maldivas"
paises_3digitos["MLI"] = "Mali"
paises_3digitos["MLT"] = "Malta"
paises_3digitos["MAR"] = "Marrocos"
paises_3digitos["MTQ"] = "Martinica"
paises_3digitos["MUS"] = "Maurício"
paises_3digitos["MRT"] = "Mauritânia"
paises_3digitos["MYT"] = "Mayotte"
paises_3digitos["MEX"] = "México"
paises_3digitos["FSM"] = "Micronésia"
paises_3digitos["MOZ"] = "Moçambique"
paises_3digitos["MDA"] = "Moldávia"
paises_3digitos["MCO"] = "Mônaco"
paises_3digitos["MNG"] = "Mongólia"
paises_3digitos["MNE"] = "Montenegro"
paises_3digitos["MSR"] = "Montserrat"
paises_3digitos["MMR"] = "Myanmar"
paises_3digitos["NAM"] = "Namíbia"
paises_3digitos["NRU"] = "Nauru"
paises_3digitos["NPL"] = "Nepal"
paises_3digitos["NIC"] = "Nicarágua"
paises_3digitos["NER"] = "Níger"
paises_3digitos["NGA"] = "Nigéria"
paises_3digitos["NIU"] = "Niue"
paises_3digitos["NOR"] = "Noruega"
paises_3digitos["NCL"] = "Nova Caledônia"
paises_3digitos["NZL"] = "Nova Zelândia"
paises_3digitos["OMN"] = "Omã"
paises_3digitos["PLW"] = "Palau"
paises_3digitos["PAN"] = "Panamá"
paises_3digitos["PNG"] = "Papua-Nova Guiné"
paises_3digitos["PAK"] = "Paquistão"
paises_3digitos["PRY"] = "Paraguai"
paises_3digitos["PER"] = "Peru"
paises_3digitos["PYF"] = "Polinésia Francesa"
paises_3digitos["POL"] = "Polônia"
paises_3digitos["PRI"] = "Porto Rico"
paises_3digitos["PRT"] = "Portugal"
paises_3digitos["QAT"] = "Qatar"
paises_3digitos["KEN"] = "Quênia"
paises_3digitos["KGZ"] = "Quirguistão"
paises_3digitos["CAF"] = "República Centro-Africana"
paises_3digitos["COD"] = "República Democrática do Congo"
paises_3digitos["DOM"] = "República Dominicana"
paises_3digitos["CZE"] = "República Checa"
paises_3digitos["ROM"] = "Romênia"
paises_3digitos["RWA"] = "Ruanda"
paises_3digitos["RUS"] = "Rússia"
paises_3digitos["ESH"] = "Saara Ocidental"
paises_3digitos["VCT"] = "São Vicente e Granadinas"
paises_3digitos["ASM"] = "Samoa Americana"
paises_3digitos["WSM"] = "Samoa Ocidental"
paises_3digitos["SMR"] = "San Marino"
paises_3digitos["SHN"] = "Santa Helena"
paises_3digitos["LCA"] = "Santa Lúcia"
paises_3digitos["BLM"] = "São Bartolomeu"
paises_3digitos["KNA"] = "São Cristóvão e Névis"
paises_3digitos["MAF"] = "São Martim"
paises_3digitos["STP"] = "São Tomé e Príncipe"
paises_3digitos["SEN"] = "Senegal"
paises_3digitos["SLE"] = "Serra Leoa"
paises_3digitos["SRB"] = "Sérvia"
paises_3digitos["SGP"] = "Singapura"
paises_3digitos["SYR"] = "Síria"
paises_3digitos["SOM"] = "Somália"
paises_3digitos["LKA"] = "Sri Lanka"
paises_3digitos["SPM"] = "São Pedro e Miquelon"
paises_3digitos["SWZ"] = "Suazilândia"
paises_3digitos["SDN"] = "Sudão"
paises_3digitos["SWE"] = "Suécia"
paises_3digitos["CHE"] = "Suíça"
paises_3digitos["SUR"] = "Suriname"
paises_3digitos["TJK"] = "Tajiquistão"
paises_3digitos["THA"] = "Tailândia"
paises_3digitos["TWN"] = "Taiwan"
paises_3digitos["TZA"] = "Tanzânia"
paises_3digitos["IOT"] = "Território Britânico do Oceano Índico"
paises_3digitos["ATF"] = "Território do Sul da França"
paises_3digitos["PSE"] = "Território Palestino Ocupado"
paises_3digitos["TMP"] = "Timor Leste"
paises_3digitos["TGO"] = "Togo"
paises_3digitos["TON"] = "Tonga"
paises_3digitos["TTO"] = "Trinidad e Tobago"
paises_3digitos["TUN"] = "Tunísia"
paises_3digitos["TKM"] = "Turcomenistão"
paises_3digitos["TUR"] = "Turquia"
paises_3digitos["TUV"] = "Tuvalu"
paises_3digitos["UKR"] = "Ucrânia"
paises_3digitos["UGA"] = "Uganda"
paises_3digitos["URY"] = "Uruguai"
paises_3digitos["UZB"] = "Usbequistão"
paises_3digitos["VUT"] = "Vanuatu"
paises_3digitos["VAT"] = "Vaticano"
paises_3digitos["VEN"] = "Venezuela"
paises_3digitos["VNM"] = "Vietnã"
paises_3digitos["ZMB"] = "Zâmbia"
paises_3digitos["ZWE"] = "Zimbabué"

# dicionario de equivalencia de siglas de países para compatibilizar com o grafico de mapa mundial
paises_3digitos_para_2 = {}
paises_3digitos_para_2["AND"] = "ad"
paises_3digitos_para_2["ARE"] = "ae"
paises_3digitos_para_2["AFG"] = "af"
paises_3digitos_para_2["ALB"] = "al"
paises_3digitos_para_2["ARM"] = "am"
paises_3digitos_para_2["AGO"] = "ao"
paises_3digitos_para_2["ATA"] = "aq"
paises_3digitos_para_2["ARG"] = "ar"
paises_3digitos_para_2["AUT"] = "at"
paises_3digitos_para_2["AUS"] = "au"
paises_3digitos_para_2["AZE"] = "az"
paises_3digitos_para_2["BIH"] = "ba"
paises_3digitos_para_2["BGD"] = "bd"
paises_3digitos_para_2["BEL"] = "be"
paises_3digitos_para_2["BFA"] = "bf"
paises_3digitos_para_2["BGR"] = "bg"
paises_3digitos_para_2["BHR"] = "bh"
paises_3digitos_para_2["BDI"] = "bi"
paises_3digitos_para_2["BEN"] = "bj"
paises_3digitos_para_2["BRN"] = "bn"
paises_3digitos_para_2["BOL"] = "bo"
paises_3digitos_para_2["BRA"] = "br"
paises_3digitos_para_2["BTN"] = "bt"
paises_3digitos_para_2["BWA"] = "bw"
paises_3digitos_para_2["BLR"] = "by"
paises_3digitos_para_2["BLZ"] = "bz"
paises_3digitos_para_2["CAN"] = "ca"
paises_3digitos_para_2["COD"] = "cd"
paises_3digitos_para_2["CAF"] = "cf"
paises_3digitos_para_2["COG"] = "cg"
paises_3digitos_para_2["CHE"] = "ch"
paises_3digitos_para_2["CIV"] = "ci"
paises_3digitos_para_2["CHL"] = "cl"
paises_3digitos_para_2["CMR"] = "cm"
paises_3digitos_para_2["CHN"] = "cn"
paises_3digitos_para_2["COL"] = "co"
paises_3digitos_para_2["CRI"] = "cr"
paises_3digitos_para_2["CUB"] = "cu"
paises_3digitos_para_2["CPV"] = "cv"
paises_3digitos_para_2["CYP"] = "cy"
paises_3digitos_para_2["CZE"] = "cz"
paises_3digitos_para_2["DEU"] = "de"
paises_3digitos_para_2["DJI"] = "dj"
paises_3digitos_para_2["DNK"] = "dk"
paises_3digitos_para_2["DOM"] = "do"
paises_3digitos_para_2["DZA"] = "dz"
paises_3digitos_para_2["ECU"] = "ec"
paises_3digitos_para_2["EST"] = "ee"
paises_3digitos_para_2["EGY"] = "eg"
paises_3digitos_para_2["ESH"] = "eh"
paises_3digitos_para_2["ERI"] = "er"
paises_3digitos_para_2["ESP"] = "es"
paises_3digitos_para_2["ETH"] = "et"
paises_3digitos_para_2["FIN"] = "fi"
paises_3digitos_para_2["FRA"] = "fr"
paises_3digitos_para_2["GAB"] = "ga"
paises_3digitos_para_2["GBR"] = "gb"
paises_3digitos_para_2["GEO"] = "ge"
paises_3digitos_para_2["GUF"] = "gf"
paises_3digitos_para_2["GHA"] = "gh"
paises_3digitos_para_2["GRL"] = "gl"
paises_3digitos_para_2["GMB"] = "gm"
paises_3digitos_para_2["GIN"] = "gn"
paises_3digitos_para_2["GNQ"] = "gq"
paises_3digitos_para_2["GRC"] = "gr"
paises_3digitos_para_2["GTM"] = "gt"
paises_3digitos_para_2["GUM"] = "gu"
paises_3digitos_para_2["GNB"] = "gw"
paises_3digitos_para_2["GUY"] = "gy"
paises_3digitos_para_2["HKG"] = "hk"
paises_3digitos_para_2["HND"] = "hn"
paises_3digitos_para_2["HRV"] = "hr"
paises_3digitos_para_2["HTI"] = "ht"
paises_3digitos_para_2["HUN"] = "hu"
paises_3digitos_para_2["IDN"] = "id"
paises_3digitos_para_2["IRL"] = "ie"
paises_3digitos_para_2["ISL"] = "il"
paises_3digitos_para_2["IND"] = "in"
paises_3digitos_para_2["IRQ"] = "iq"
paises_3digitos_para_2["IRN"] = "ir"
paises_3digitos_para_2["ISL"] = "is"
paises_3digitos_para_2["ITA"] = "it"
paises_3digitos_para_2["JAM"] = "jm"
paises_3digitos_para_2["JOR"] = "jo"
paises_3digitos_para_2["JPN"] = "jp"
paises_3digitos_para_2["KEN"] = "ke"
paises_3digitos_para_2["KGZ"] = "kg"
paises_3digitos_para_2["KHM"] = "kh"
paises_3digitos_para_2["PRK"] = "kp"
paises_3digitos_para_2["KOR"] = "kr"
paises_3digitos_para_2["KWT"] = "kw"
paises_3digitos_para_2["KAZ"] = "kz"
paises_3digitos_para_2["LAO"] = "la"
paises_3digitos_para_2["LBN"] = "lb"
paises_3digitos_para_2["LIE"] = "li"
paises_3digitos_para_2["LKA"] = "lk"
paises_3digitos_para_2["LBR"] = "lr"
paises_3digitos_para_2["LSO"] = "ls"
paises_3digitos_para_2["LTU"] = "lt"
paises_3digitos_para_2["LUX"] = "lu"
paises_3digitos_para_2["LVA"] = "lv"
paises_3digitos_para_2["LBY"] = "ly"
paises_3digitos_para_2["MAR"] = "ma"
paises_3digitos_para_2["MCO"] = "mc"
paises_3digitos_para_2["MDA"] = "md"
paises_3digitos_para_2["MNE"] = "me"
paises_3digitos_para_2["MDG"] = "mg"
paises_3digitos_para_2["MKD"] = "mk"
paises_3digitos_para_2["MLI"] = "ml"
paises_3digitos_para_2["MMR"] = "mm"
paises_3digitos_para_2["MNG"] = "mn"
paises_3digitos_para_2["MAC"] = "mo"
paises_3digitos_para_2["MRT"] = "mr"
paises_3digitos_para_2["MLT"] = "mt"
paises_3digitos_para_2["MUS"] = "mu"
paises_3digitos_para_2["MDV"] = "mv"
paises_3digitos_para_2["MWI"] = "mw"
paises_3digitos_para_2["MEX"] = "mx"
paises_3digitos_para_2["MYS"] = "my"
paises_3digitos_para_2["MOZ"] = "mz"
paises_3digitos_para_2["NAM"] = "na"
paises_3digitos_para_2["NER"] = "ne"
paises_3digitos_para_2["NGA"] = "ng"
paises_3digitos_para_2["NIC"] = "ni"
paises_3digitos_para_2["NLD"] = "nl"
paises_3digitos_para_2["NOR"] = "no"
paises_3digitos_para_2["NPL"] = "np"
paises_3digitos_para_2["NZL"] = "nz"
paises_3digitos_para_2["OMN"] = "om"
paises_3digitos_para_2["PAN"] = "pa"
paises_3digitos_para_2["PER"] = "pe"
paises_3digitos_para_2["PNG"] = "pg"
paises_3digitos_para_2["PHL"] = "ph"
paises_3digitos_para_2["PAK"] = "pk"
paises_3digitos_para_2["POL"] = "pl"
paises_3digitos_para_2["PRI"] = "pr"
paises_3digitos_para_2["PSE"] = "ps"
paises_3digitos_para_2["PRT"] = "pt"
paises_3digitos_para_2["PRY"] = "py"
paises_3digitos_para_2["REU"] = "re"
paises_3digitos_para_2["ROM"] = "ro"
paises_3digitos_para_2["SRB"] = "rs"
paises_3digitos_para_2["RUS"] = "ru"
paises_3digitos_para_2["RWA"] = "rw"
paises_3digitos_para_2["SAU"] = "sa"
paises_3digitos_para_2["SYC"] = "sc"
paises_3digitos_para_2["SDN"] = "sd"
paises_3digitos_para_2["SWE"] = "se"
paises_3digitos_para_2["SGP"] = "sg"
paises_3digitos_para_2["SHN"] = "sh"
paises_3digitos_para_2["SVN"] = "si"
paises_3digitos_para_2["SVK"] = "sk"
paises_3digitos_para_2["SLE"] = "sl"
paises_3digitos_para_2["SMR"] = "sm"
paises_3digitos_para_2["SEN"] = "sn"
paises_3digitos_para_2["SOM"] = "so"
paises_3digitos_para_2["SUR"] = "sr"
paises_3digitos_para_2["STP"] = "st"
paises_3digitos_para_2["SLV"] = "sv"
paises_3digitos_para_2["SYR"] = "sy"
paises_3digitos_para_2["SWZ"] = "sz"
paises_3digitos_para_2["TCD"] = "td"
paises_3digitos_para_2["TGO"] = "tg"
paises_3digitos_para_2["THA"] = "th"
paises_3digitos_para_2["TJK"] = "tj"
paises_3digitos_para_2["TLS"] = "tl"
paises_3digitos_para_2["TKM"] = "tm"
paises_3digitos_para_2["TUN"] = "tn"
paises_3digitos_para_2["TUR"] = "tr"
paises_3digitos_para_2["TWN"] = "tw"
paises_3digitos_para_2["TZA"] = "tz"
paises_3digitos_para_2["UKR"] = "ua"
paises_3digitos_para_2["UGA"] = "ug"
paises_3digitos_para_2["USA"] = "us"
paises_3digitos_para_2["URY"] = "uy"
paises_3digitos_para_2["UZB"] = "uz"
paises_3digitos_para_2["VAT"] = "va"
paises_3digitos_para_2["VEN"] = "ve"
paises_3digitos_para_2["VNM"] = "vn"
paises_3digitos_para_2["YEM"] = "ye"
paises_3digitos_para_2["MYT"] = "yt"
paises_3digitos_para_2["ZAF"] = "za"
paises_3digitos_para_2["ZMB"] = "zm"
paises_3digitos_para_2["ZWE"] = "zw"

# funcoes uteis para leitura os arquivos CSV
def importa_csv_para_lista(arq):
    print("Importando o arquivo: " + arq + " para estrutura de dados em memória a fim de permitir análise.")
    with open(arq, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter=';')
        lista = list(reader)
    print("Concluído.")
    return lista

def importa_csv_para_dicionario(arq):
    print("Importando o arquivo: " + arq + " para estrutura de dados em memória a fim de permitir análise.")
    dicionario = {}
    reader = csv.reader(open(arq, 'r', encoding='latin-1'))
    for row in reader:
        aux_linha = row[0]
        aux_linha_str = aux_linha.split(";")
        chave = aux_linha_str[0]
        valor = aux_linha_str[1]
        dicionario[chave] = valor
    print("Concluído.")
    return dicionario

# https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string/517974#517974
def remover_acentos(texto):
    unaccented_string = unidecode.unidecode(texto)
    return unaccented_string

def sigla_para_mapa_mundi():
    pVez = True
    d = datetime.date.today()
    mes = d.month
    ano = d.year
    resp = "'" + str(mes) + "/" + str(ano) + "'" + "," + " {"
    for key, value in nacionalidade_dict.items():
        chave = paises_3digitos_para_2.get(key)
        if (chave is not None):
            if (pVez):
                resp = resp + '{}{}{}{} {}{}{}'.format( "'", chave, "'", ":", "int(", value, ")" )  + "\n"
            else:
                resp = resp + '{}{}{}{}{} {}{}{}'.format(",", "'", chave, "'", ":", "int(", value, ")" ) + "\n"

        pVez = False
    resp = resp + "}"
    return resp

# lista para receber o arquivo numero_identificador_lattes_zzzz.csv
identificador_list_cvs = list()
# dicionario para receber o arquivo tab_area_conhecimento_zzzz.csv
area_dict_csv = {}
# dicionario para receber o arquivo tab_nivel_formacao_zzzz.csv
nivel_formacao_dict_csv = {}

# url dos arquivos da plataforma lattes, disponivel em:  http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados
url = "http://memoria.cnpq.br/documents/313759/6935115b-a5e8-4cfb-96cf-00e2fd11c96c"
print("URL lattes: " + url)

# definicao do arquivo destino na maquina do usuario
arquivo_lattes = os.path.expanduser("~/lattes.zip")
print("Arquivo de download destino: " + arquivo_lattes)

dir_destino = os.path.dirname(arquivo_lattes)
print("Diretório de trabalho local: " + dir_destino)

print("Iniciando download do arquivo na plataforma lattes. Processo demorado...")
urllib.request.urlretrieve(url, arquivo_lattes)
print("Download concluído: " + arquivo_lattes)

print("Descompactando o arquivo ZIP... ")
with zipfile.ZipFile(arquivo_lattes, "r") as zip_ref:
    zip_ref.extractall(dir_destino)
print("Arquivos da plataforma lattes extraídos em: " + dir_destino)

for file in os.listdir(dir_destino):
    if file.endswith(".csv"):
        if file.startswith("numero_identificador_lattes"):
            identificador_arq = os.path.join(dir_destino, file)
            identificador_list_cvs = importa_csv_para_lista(identificador_arq)

        if file.startswith("tab_area_conhecimento"):
            area_arq = os.path.join(dir_destino, file)
            area_dict_csv = importa_csv_para_dicionario(area_arq)

        if file.startswith("tab_nivel_formacao"):
            nivel_arq = os.path.join(dir_destino, file)
            nivel_formacao_dict_csv = importa_csv_para_dicionario(nivel_arq)

# o algoritmo deve varrer a lista do identificador que eh o arquivo principal
# analisar cada linha do arquivo e trabalhar com geraçao estatistica
# em estruturas de dados em python, denominadas dicionario

nacionalidade_dict = {}
area_conhecimento_dict = {}
nivel_formacao_dict = {}

# processando o arquivo identificador para geracao de listas e estatisticas
print("Processando arquivo identificador (Lattes). Processo demorado...")
i = 1
valor = 0
while i < len(identificador_list_cvs):
    # le a linha
    aux_linha = identificador_list_cvs[i]
    # e extrai as strings para cada estatistica
    aux_nacionalidade = aux_linha[1]
    aux_area = aux_linha[3]
    aux_nivel = aux_linha[4]

    # trata a estatistica da nacionalidade
    valor_nacionalidade = nacionalidade_dict.get(aux_nacionalidade)
    if valor_nacionalidade is None:
        nacionalidade_dict[aux_nacionalidade] = 1
    else:
        valor_nacionalidade = valor_nacionalidade + 1
        nacionalidade_dict[aux_nacionalidade] = valor_nacionalidade

    # trata a estatistica da area de conhecimento
    valor_area = area_conhecimento_dict.get(aux_area)
    if valor_area is None:
        area_conhecimento_dict[aux_area] = 1
    else:
        valor_area = valor_area + 1
        area_conhecimento_dict[aux_area] = valor_area

    # trata a estatistica do nivel de formacao
    valor_nivel = nivel_formacao_dict.get(aux_nivel)
    if valor_nivel is None:
        nivel_formacao_dict[aux_nivel] = 1
    else:
        valor_nivel = valor_nivel + 1
        nivel_formacao_dict[aux_nivel] = valor_nivel

    i = i + 1


# migrar os dicionarios para estruturas de listas
# a fim de permitir ordenacao e gerar graficos para melhor leitura
nacionalidade_list = list()
print( "Ordenando a lista de nacionalidade..." )
nacionalidade_list = sorted(nacionalidade_dict.items(), key = lambda x: x[1], reverse=True )

area_list = list()
print ( "Ordenando a lista de área de atuação..." )
area_list = sorted(area_conhecimento_dict.items(), key = lambda x: x[1], reverse=True)

nivel_formacao_list = list()
print( "Ordenando a lista de nível de formação..." )
nivel_formacao_list = sorted(nivel_formacao_dict.items(), key = lambda x: x[1], reverse=True)

# ######################################################
# GRAFICOS
# ######################################################

print( "Gerando os gráficos estatísticos" )

# gerar o grafico de barras de pesquisadores estrageiros
nacionalidade_chart = pygal.HorizontalBar()
nacionalidade_chart.title = 'Pesquisadores estrangeiros cadastrados na Plataforma Lattes'
i = 0
while i < len(nacionalidade_list):
    aux_linha = nacionalidade_list[i]
    aux_nacionalidade = aux_linha[0]
    aux_nacionalidade_extenso = paises_3digitos.get(aux_nacionalidade)

    if (aux_nacionalidade_extenso is None):
       aux_nacionalidade_extenso =  aux_nacionalidade
    else:
        aux_nacionalidade_extenso = remover_acentos( aux_nacionalidade_extenso )

    valor_nacionalidade = aux_linha[1]
    if aux_nacionalidade != "BRA":
        nacionalidade_chart.add(aux_nacionalidade_extenso, valor_nacionalidade)
    else:
        print()
        print( "[!] Número de pesquisadores Brasileiros cadastrados: " + str(valor_nacionalidade) )
        print()
    i = i + 1
nacionalidade_chart.render_in_browser()

# gerar o grafico de area de atuaçao
area_chart = pygal.HorizontalBar()
area_chart.title = "Area de atuacao dos pesquisadores"
i = 0
while i < len(area_list):
    aux_linha = area_list[i]
    aux_area = aux_linha[0]
    aux_area_extenso = area_dict_csv.get(aux_area)
    valor_area = aux_linha[1]
    if bool(aux_area_extenso and aux_area_extenso.strip()):
        aux_area_extenso = remover_acentos( aux_area_extenso )
        area_chart.add(aux_area_extenso, valor_area)
    i = i + 1
area_chart.render_in_browser()

# gerar o grafico de nivel de formacao
nivel_formacao_chart = pygal.HorizontalBar()
nivel_formacao_chart.title = "Nivel de formacao dos pesquisadores"
i = 0
while i < len(nivel_formacao_list):
    aux_linha = nivel_formacao_list[i]
    aux_nivel = aux_linha[0]
    if (bool(aux_nivel and aux_nivel.strip())):
        aux_nivel_extenso = nivel_formacao_dict_csv.get(aux_nivel)
        aux_nivel_extenso = remover_acentos( aux_nivel_extenso )
    else:
        aux_nivel_extenso = "Nao informado"
    valor_nivel = aux_linha[1]
    nivel_formacao_chart.add(aux_nivel_extenso, valor_nivel)
    i = i + 1
nivel_formacao_chart.render_in_browser()

# gerar o grafico mapa mundi de forma ESTÁTICA
# porque o metodo add NAO aceita o retorno da funcao de geracao dinamica: sigla_para_mapa_mundi()
# estou pesquisando como solucionar essa situacao
#print( sigla_para_mapa_mundi() )
print("Mapa gerado em Dez/2017")
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = ('Pesquisadores cadastrados na plataforma Lattes - por paises.')
worldmap_chart.add(
'12/2017', {'br': int(5129564)
,'cz': int(57)
,'be': int(315)
,'cn': int(482)
,'it': int(2383)
,'cl': int(2019)
,'jp': int(343)
,'cu': int(2628)
,'uy': int(1368)
,'pt': int(5033)
,'nl': int(431)
,'co': int(9424)
,'gw': int(1110)
,'mz': int(2462)
,'py': int(1212)
,'tr': int(76)
,'es': int(2865)
,'cv': int(1218)
,'ar': int(4411)
,'de': int(1912)
,'gb': int(420)
,'za': int(59)
,'fr': int(2424)
,'pe': int(5879)
,'tl': int(188)
,'ao': int(1626)
,'in': int(956)
,'cr': int(298)
,'ch': int(203)
,'bg': int(72)
,'bo': int(1336)
,'nz': int(40)
,'us': int(2585)
,'ng': int(354)
,'ci': int(46)
,'ec': int(1001)
,'ca': int(562)
,'ke': int(47)
,'mx': int(1238)
,'ve': int(1290)
,'ir': int(358)
,'pk': int(1011)
,'hn': int(177)
,'st': int(251)
,'et': int(104)
,'sv': int(126)
,'eg': int(213)
,'tn': int(42)
,'gt': int(136)
,'no': int(73)
,'dz': int(41)
,'th': int(14)
,'ga': int(20)
,'id': int(27)
,'np': int(17)
,'hu': int(75)
,'ly': int(17)
,'bd': int(33)
,'at': int(144)
,'ie': int(92)
,'cd': int(92)
,'cm': int(170)
,'gh': int(78)
,'ni': int(134)
,'bj': int(231)
,'pa': int(151)
,'uz': int(20)
,'ua': int(105)
,'tg': int(29)
,'do': int(195)
,'kr': int(210)
,'pl': int(198)
,'cg': int(49)
,'ma': int(54)
,'se': int(131)
,'ru': int(390)
,'lb': int(74)
,'ht': int(231)
,'fi': int(66)
,'by': int(39)
,'gr': int(128)
,'dk': int(97)
,'rs': int(49)
,'au': int(223)
,'jo': int(20)
,'my': int(21)
,'sd': int(36)
,'sn': int(68)
,'tm': int(1)
,'zw': int(7)
,'sy': int(60)
,'si': int(26)
,'lt': int(10)
,'gf': int(3)
,'sr': int(36)
,'ph': int(20)
,'bf': int(12)
,'iq': int(27)
,'sg': int(8)
,'gn': int(8)
,'al': int(7)
,'hr': int(32)
,'lu': int(10)
,'gy': int(13)
,'tz': int(26)
,'ug': int(9)
,'tw': int(61)
,'mg': int(10)
,'jm': int(25)
,'bw': int(3)
,'am': int(30)
,'pr': int(18)
,'hk': int(14)
,'td': int(4)
,'ee': int(8)
,'lv': int(9)
,'is': int(3)
,'af': int(7)
,'ne': int(8)
,'va': int(4)
,'na': int(6)
,'sa': int(4)
,'sk': int(30)
,'ad': int(3)
,'ge': int(9)
,'mt': int(2)
,'zm': int(9)
,'lk': int(7)
,'rw': int(9)
,'mu': int(5)
,'vn': int(16)
,'mw': int(3)
,'mk': int(8)
,'kw': int(1)
,'sl': int(2)
,'bz': int(3)
,'cy': int(4)
,'lr': int(2)
,'mr': int(4)
,'ba': int(3)
,'kz': int(5)
,'az': int(3)
,'mn': int(3)
,'md': int(5)
,'kp': int(1)
,'ml': int(9)
,'bt': int(3)
,'ye': int(2)
,'ae': int(1)
,'mo': int(3)
,'me': int(1)
,'om': int(1)
,'mm': int(1)
,'la': int(3)
,'aq': int(2)
,'kh': int(1)
,'gq': int(1)
,'tj': int(1)
})
worldmap_chart.render_in_browser()

#############
# FECHAMENTO
#############

# excluir os arquivos de download no final do processo
print("Excluindo o arquivo: " + arquivo_lattes )
os.remove(arquivo_lattes)
print("Excluindo o arquivo: " + identificador_arq)
os.remove(identificador_arq)
print("Excluindo o arquivo: " + area_arq)
os.remove(area_arq)
print("Excluindo o arquivo: " + nivel_arq)
os.remove(nivel_arq)

