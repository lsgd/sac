"""
Price information per SAC section from their website.

How to update the price table?

1. Go to https://www.sac-cas.ch/de/mitgliedschaft/mitglied-werden/
2. search for a section like "SAC Baldern".
3. Copy the JSON related to the section prices like you see below.
4. Optional: Format it nicely
5. Put the JSON here as a variable.
   Since this JSON and Python dictionaries are compatible, you can just use it as a dictionary out-of-the-box.
"""


prices = {
    "sectionPrices": [{
        "id": "6",
        "cantonId": "VD",
        "name": "CAS Argentine",
        "youth": {
            "yearly": 63,
            "oneTime": 0,
            "total": 63
        },
        "single": {
            "yearly": 120,
            "oneTime": 30,
            "total": 150
        },
        "family": {
            "yearly": 185,
            "oneTime": 45,
            "total": 230
        }
    }, {
        "id": "71",
        "cantonId": "TI",
        "name": "CAS Bellinzona e Valli",
        "youth": {
            "yearly": 30,
            "oneTime": 0,
            "total": 30
        },
        "single": {
            "yearly": 107,
            "oneTime": 23,
            "total": 130
        },
        "family": {
            "yearly": 155,
            "oneTime": 35,
            "total": 190
        }
    }, {
        "id": "28",
        "cantonId": "GE",
        "name": "CAS Carougeoise",
        "youth": {
            "yearly": 45,
            "oneTime": 0,
            "total": 45
        },
        "single": {
            "yearly": 122,
            "oneTime": 30,
            "total": 152
        },
        "family": {
            "yearly": 195,
            "oneTime": 50,
            "total": 245
        }
    }, {
        "id": "29",
        "cantonId": "BE",
        "name": "CAS Chasseral",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 203,
            "oneTime": 30,
            "total": 233
        }
    }, {
        "id": "30",
        "cantonId": "VS",
        "name": "CAS Chasseron",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 190,
            "oneTime": 30,
            "total": 220
        }
    }, {
        "id": "31",
        "cantonId": "VD",
        "name": "CAS Chaussy",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 145,
            "oneTime": 20,
            "total": 165
        },
        "family": {
            "yearly": 222,
            "oneTime": 30,
            "total": 252
        }
    }, {
        "id": "34",
        "cantonId": "JU",
        "name": "CAS Del\u00e9mont",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 111,
            "oneTime": 25,
            "total": 136
        },
        "family": {
            "yearly": 175,
            "oneTime": 39,
            "total": 214
        }
    }, {
        "id": "35",
        "cantonId": "FR",
        "name": "CAS Dent-De-Lys",
        "youth": {
            "yearly": 68,
            "oneTime": 5,
            "total": 73
        },
        "single": {
            "yearly": 126,
            "oneTime": 25,
            "total": 151
        },
        "family": {
            "yearly": 186,
            "oneTime": 40,
            "total": 226
        }
    }, {
        "id": "40",
        "cantonId": "VD",
        "name": "CAS Diabl. Ch\u00e2teau d\u0027Oex",
        "youth": {
            "yearly": 85,
            "oneTime": 0,
            "total": 85
        },
        "single": {
            "yearly": 160,
            "oneTime": 50,
            "total": 210
        },
        "family": {
            "yearly": 257,
            "oneTime": 90,
            "total": 347
        }
    }, {
        "id": "36",
        "cantonId": "VD",
        "name": "CAS Diablerets Lausanne",
        "youth": {
            "yearly": 95,
            "oneTime": 0,
            "total": 95
        },
        "single": {
            "yearly": 185,
            "oneTime": 50,
            "total": 235
        },
        "family": {
            "yearly": 287,
            "oneTime": 90,
            "total": 377
        }
    }, {
        "id": "37",
        "cantonId": "VD",
        "name": "CAS Diablerets Morges",
        "youth": {
            "yearly": 85,
            "oneTime": 0,
            "total": 85
        },
        "single": {
            "yearly": 165,
            "oneTime": 50,
            "total": 215
        },
        "family": {
            "yearly": 267,
            "oneTime": 90,
            "total": 357
        }
    }, {
        "id": "38",
        "cantonId": "VD",
        "name": "CAS Diablerets Payerne",
        "youth": {
            "yearly": 80,
            "oneTime": 0,
            "total": 80
        },
        "single": {
            "yearly": 160,
            "oneTime": 50,
            "total": 210
        },
        "family": {
            "yearly": 260,
            "oneTime": 90,
            "total": 350
        }
    }, {
        "id": "39",
        "cantonId": "VD",
        "name": "CAS Diablerets Vallorbe",
        "youth": {
            "yearly": 85,
            "oneTime": 0,
            "total": 85
        },
        "single": {
            "yearly": 175,
            "oneTime": 50,
            "total": 225
        },
        "family": {
            "yearly": 287,
            "oneTime": 90,
            "total": 377
        }
    }, {
        "id": "49",
        "cantonId": "GE",
        "name": "CAS Genevoise",
        "youth": {
            "yearly": 45,
            "oneTime": 0,
            "total": 45
        },
        "single": {
            "yearly": 140,
            "oneTime": 20,
            "total": 160
        },
        "family": {
            "yearly": 214,
            "oneTime": 30,
            "total": 244
        }
    }, {
        "id": "54",
        "cantonId": "FR",
        "name": "CAS Gruy\u00e8re",
        "youth": {
            "yearly": 70,
            "oneTime": 0,
            "total": 70
        },
        "single": {
            "yearly": 115,
            "oneTime": 55,
            "total": 170
        },
        "family": {
            "yearly": 190,
            "oneTime": 90,
            "total": 280
        }
    }, {
        "id": "61",
        "cantonId": "VD",
        "name": "CAS Jaman",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 160,
            "oneTime": 70,
            "total": 230
        },
        "family": {
            "yearly": 240,
            "oneTime": 80,
            "total": 320
        }
    }, {
        "id": "63",
        "cantonId": "JU",
        "name": "CAS Jura",
        "youth": {
            "yearly": 47,
            "oneTime": 5,
            "total": 52
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 188,
            "oneTime": 30,
            "total": 218
        }
    }, {
        "id": "32",
        "cantonId": "NE",
        "name": "CAS La Chaux-de-Fonds",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 135,
            "oneTime": 40,
            "total": 175
        },
        "family": {
            "yearly": 212,
            "oneTime": 50,
            "total": 262
        }
    }, {
        "id": "41",
        "cantonId": "VD",
        "name": "CAS La D\u00f4le",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 115,
            "oneTime": 55,
            "total": 170
        },
        "family": {
            "yearly": 180,
            "oneTime": 100,
            "total": 280
        }
    }, {
        "id": "17",
        "cantonId": "BE",
        "name": "CAS La Neuveville",
        "youth": {
            "yearly": 63,
            "oneTime": 0,
            "total": 63
        },
        "single": {
            "yearly": 128,
            "oneTime": 20,
            "total": 148
        },
        "family": {
            "yearly": 191,
            "oneTime": 30,
            "total": 221
        }
    }, {
        "id": "73",
        "cantonId": "TI",
        "name": "CAS Locarno",
        "youth": {
            "yearly": 35,
            "oneTime": 0,
            "total": 35
        },
        "single": {
            "yearly": 97,
            "oneTime": 20,
            "total": 117
        },
        "family": {
            "yearly": 149,
            "oneTime": 30,
            "total": 179
        }
    }, {
        "id": "75",
        "cantonId": "FR",
        "name": "CAS Mol\u00e9son",
        "youth": {
            "yearly": 60,
            "oneTime": 10,
            "total": 70
        },
        "single": {
            "yearly": 135,
            "oneTime": 40,
            "total": 175
        },
        "family": {
            "yearly": 205,
            "oneTime": 60,
            "total": 265
        }
    }, {
        "id": "76",
        "cantonId": "VS",
        "name": "CAS Montana-Vermala",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 110,
            "oneTime": 70,
            "total": 180
        },
        "family": {
            "yearly": 164,
            "oneTime": 110,
            "total": 274
        }
    }, {
        "id": "80",
        "cantonId": "VS",
        "name": "CAS Monte Rosa Martigny",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "78",
        "cantonId": "VS",
        "name": "CAS Monte Rosa Monthey",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "82",
        "cantonId": "VS",
        "name": "CAS Monte Rosa Sierre",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "81",
        "cantonId": "VS",
        "name": "CAS Monte Rosa Sion",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "79",
        "cantonId": "VS",
        "name": "CAS Monte Rosa St-Maurice",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "87",
        "cantonId": "VD",
        "name": "CAS Montreux",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 130,
            "oneTime": 30,
            "total": 160
        },
        "family": {
            "yearly": 212,
            "oneTime": 40,
            "total": 252
        }
    }, {
        "id": "89",
        "cantonId": "NE",
        "name": "CAS Neuch\u00e2teloise",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 121,
            "oneTime": 30,
            "total": 151
        },
        "family": {
            "yearly": 200,
            "oneTime": 50,
            "total": 250
        }
    }, {
        "id": "100",
        "cantonId": "BE",
        "name": "CAS Pierre-Pertuis",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 114,
            "oneTime": 40,
            "total": 154
        },
        "family": {
            "yearly": 192,
            "oneTime": 60,
            "total": 252
        }
    }, {
        "id": "111",
        "cantonId": "BE",
        "name": "CAS Pr\u00e9v\u00f4toise",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 115,
            "oneTime": 30,
            "total": 145
        },
        "family": {
            "yearly": 180,
            "oneTime": 40,
            "total": 220
        }
    }, {
        "id": "112",
        "cantonId": "JU",
        "name": "CAS Raimeux",
        "youth": {
            "yearly": 56,
            "oneTime": 0,
            "total": 56
        },
        "single": {
            "yearly": 101,
            "oneTime": 20,
            "total": 121
        },
        "family": {
            "yearly": 139,
            "oneTime": 30,
            "total": 169
        }
    }, {
        "id": "123",
        "cantonId": "NE",
        "name": "CAS Sommartel",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 121,
            "oneTime": 85,
            "total": 206
        },
        "family": {
            "yearly": 186,
            "oneTime": 95,
            "total": 281
        }
    }, {
        "id": "127",
        "cantonId": "TI",
        "name": "CAS Ticino",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 105,
            "oneTime": 30,
            "total": 135
        },
        "family": {
            "yearly": 179,
            "oneTime": 50,
            "total": 229
        }
    }, {
        "id": "133",
        "cantonId": "VD",
        "name": "CAS Val-De-Joux",
        "youth": {
            "yearly": 45,
            "oneTime": 15,
            "total": 60
        },
        "single": {
            "yearly": 100,
            "oneTime": 25,
            "total": 125
        },
        "family": {
            "yearly": 150,
            "oneTime": 40,
            "total": 190
        }
    }, {
        "id": "139",
        "cantonId": "VD",
        "name": "CAS Yverdon",
        "youth": {
            "yearly": 70,
            "oneTime": 0,
            "total": 70
        },
        "single": {
            "yearly": 135,
            "oneTime": 60,
            "total": 195
        },
        "family": {
            "yearly": 222,
            "oneTime": 70,
            "total": 292
        }
    }, {
        "id": "2",
        "cantonId": "AG",
        "name": "SAC Aarau",
        "youth": {
            "yearly": 58,
            "oneTime": 0,
            "total": 58
        },
        "single": {
            "yearly": 112,
            "oneTime": 30,
            "total": 142
        },
        "family": {
            "yearly": 180,
            "oneTime": 40,
            "total": 220
        }
    }, {
        "id": "4",
        "cantonId": "BE",
        "name": "SAC Altels",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 106,
            "oneTime": 20,
            "total": 126
        },
        "family": {
            "yearly": 168,
            "oneTime": 30,
            "total": 198
        }
    }, {
        "id": "3",
        "cantonId": "ZH",
        "name": "SAC Am Albis",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 145,
            "oneTime": 50,
            "total": 195
        },
        "family": {
            "yearly": 230,
            "oneTime": 60,
            "total": 290
        }
    }, {
        "id": "5",
        "cantonId": "BS",
        "name": "SAC Angenstein",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 135,
            "oneTime": 50,
            "total": 185
        },
        "family": {
            "yearly": 198,
            "oneTime": 30,
            "total": 228
        }
    }, {
        "id": "7",
        "cantonId": "GR",
        "name": "SAC Arosa",
        "youth": {
            "yearly": 30,
            "oneTime": 0,
            "total": 30
        },
        "single": {
            "yearly": 100,
            "oneTime": 20,
            "total": 120
        },
        "family": {
            "yearly": 145,
            "oneTime": 30,
            "total": 175
        }
    }, {
        "id": "8",
        "cantonId": "ZH",
        "name": "SAC Bachtel",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 135,
            "oneTime": 30,
            "total": 165
        },
        "family": {
            "yearly": 200,
            "oneTime": 40,
            "total": 240
        }
    }, {
        "id": "9",
        "cantonId": "ZH",
        "name": "SAC Baldern",
        "youth": {
            "yearly": 58,
            "oneTime": 0,
            "total": 58
        },
        "single": {
            "yearly": 128,
            "oneTime": 30,
            "total": 158
        },
        "family": {
            "yearly": 216,
            "oneTime": 50,
            "total": 266
        }
    }, {
        "id": "10",
        "cantonId": "BS",
        "name": "SAC Basel",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 197,
            "oneTime": 30,
            "total": 227
        }
    }, {
        "id": "11",
        "cantonId": "BL",
        "name": "SAC Baselland",
        "youth": {
            "yearly": 55,
            "oneTime": 10,
            "total": 65
        },
        "single": {
            "yearly": 117,
            "oneTime": 30,
            "total": 147
        },
        "family": {
            "yearly": 194,
            "oneTime": 40,
            "total": 234
        }
    }, {
        "id": "12",
        "cantonId": "BE",
        "name": "SAC Bern",
        "youth": {
            "yearly": 64,
            "oneTime": 0,
            "total": 64
        },
        "single": {
            "yearly": 144,
            "oneTime": 55,
            "total": 199
        },
        "family": {
            "yearly": 223,
            "oneTime": 72,
            "total": 295
        }
    }, {
        "id": "14",
        "cantonId": "GR",
        "name": "SAC Bernina",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 107,
            "oneTime": 20,
            "total": 127
        },
        "family": {
            "yearly": 179,
            "oneTime": 30,
            "total": 209
        }
    }, {
        "id": "15",
        "cantonId": "BE",
        "name": "SAC Biel",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 145,
            "oneTime": 40,
            "total": 185
        },
        "family": {
            "yearly": 205,
            "oneTime": 60,
            "total": 265
        }
    }, {
        "id": "18",
        "cantonId": "BE",
        "name": "SAC Biel B\u00fcren a\/A",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 145,
            "oneTime": 40,
            "total": 185
        },
        "family": {
            "yearly": 205,
            "oneTime": 60,
            "total": 265
        }
    }, {
        "id": "19",
        "cantonId": "BE",
        "name": "SAC Bl\u00fcmlisalp",
        "youth": {
            "yearly": 90,
            "oneTime": 0,
            "total": 90
        },
        "single": {
            "yearly": 135,
            "oneTime": 26,
            "total": 161
        },
        "family": {
            "yearly": 230,
            "oneTime": 36,
            "total": 266
        }
    }, {
        "id": "20",
        "cantonId": "VS",
        "name": "SAC Bl\u00fcmlisalp Ausserberg",
        "youth": {
            "yearly": 90,
            "oneTime": 0,
            "total": 90
        },
        "single": {
            "yearly": 135,
            "oneTime": 26,
            "total": 161
        },
        "family": {
            "yearly": 230,
            "oneTime": 36,
            "total": 266
        }
    }, {
        "id": "21",
        "cantonId": "TG",
        "name": "SAC Bodan",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 130,
            "oneTime": 20,
            "total": 150
        },
        "family": {
            "yearly": 201,
            "oneTime": 30,
            "total": 231
        }
    }, {
        "id": "25",
        "cantonId": "BE",
        "name": "SAC Brandis",
        "youth": {
            "yearly": 51,
            "oneTime": 0,
            "total": 51
        },
        "single": {
            "yearly": 106,
            "oneTime": 20,
            "total": 126
        },
        "family": {
            "yearly": 172,
            "oneTime": 30,
            "total": 202
        }
    }, {
        "id": "22",
        "cantonId": "GR",
        "name": "SAC Bregaglia",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 97,
            "oneTime": 20,
            "total": 117
        },
        "family": {
            "yearly": 145,
            "oneTime": 30,
            "total": 175
        }
    }, {
        "id": "23",
        "cantonId": "AG",
        "name": "SAC Brugg",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 117,
            "oneTime": 50,
            "total": 167
        },
        "family": {
            "yearly": 197,
            "oneTime": 80,
            "total": 277
        }
    }, {
        "id": "24",
        "cantonId": "BE",
        "name": "SAC Burgdorf",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 192,
            "oneTime": 30,
            "total": 222
        }
    }, {
        "id": "27",
        "cantonId": "BE",
        "name": "SAC Burgdorf Damen",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 192,
            "oneTime": 30,
            "total": 222
        }
    }, {
        "id": "33",
        "cantonId": "GR",
        "name": "SAC Davos",
        "youth": {
            "yearly": 60,
            "oneTime": 10,
            "total": 70
        },
        "single": {
            "yearly": 125,
            "oneTime": 30,
            "total": 155
        },
        "family": {
            "yearly": 192,
            "oneTime": 40,
            "total": 232
        }
    }, {
        "id": "43",
        "cantonId": "SZ",
        "name": "SAC Einsiedeln",
        "youth": {
            "yearly": 33,
            "oneTime": 0,
            "total": 33
        },
        "single": {
            "yearly": 109,
            "oneTime": 20,
            "total": 129
        },
        "family": {
            "yearly": 178,
            "oneTime": 30,
            "total": 208
        }
    }, {
        "id": "44",
        "cantonId": "BE",
        "name": "SAC Emmental",
        "youth": {
            "yearly": 70,
            "oneTime": 0,
            "total": 70
        },
        "single": {
            "yearly": 130,
            "oneTime": 20,
            "total": 150
        },
        "family": {
            "yearly": 204,
            "oneTime": 30,
            "total": 234
        }
    }, {
        "id": "46",
        "cantonId": "OW",
        "name": "SAC Engelberg",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 110,
            "oneTime": 40,
            "total": 150
        },
        "family": {
            "yearly": 175,
            "oneTime": 60,
            "total": 235
        }
    }, {
        "id": "47",
        "cantonId": "GR",
        "name": "SAC Engiadina Bassa",
        "youth": {
            "yearly": 49,
            "oneTime": 0,
            "total": 49
        },
        "single": {
            "yearly": 107,
            "oneTime": 20,
            "total": 127
        },
        "family": {
            "yearly": 170,
            "oneTime": 30,
            "total": 200
        }
    }, {
        "id": "48",
        "cantonId": "LU",
        "name": "SAC Entlebuch",
        "youth": {
            "yearly": 48,
            "oneTime": 0,
            "total": 48
        },
        "single": {
            "yearly": 108,
            "oneTime": 30,
            "total": 138
        },
        "family": {
            "yearly": 176,
            "oneTime": 40,
            "total": 216
        }
    }, {
        "id": "13",
        "cantonId": "BE",
        "name": "SAC Gantrisch",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 136,
            "oneTime": 40,
            "total": 176
        },
        "family": {
            "yearly": 210,
            "oneTime": 60,
            "total": 270
        }
    }, {
        "id": "50",
        "cantonId": "UR",
        "name": "SAC Gotthard",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 110,
            "oneTime": 30,
            "total": 140
        },
        "family": {
            "yearly": 165,
            "oneTime": 45,
            "total": 210
        }
    }, {
        "id": "52",
        "cantonId": "SO",
        "name": "SAC Grenchen",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 118,
            "oneTime": 20,
            "total": 138
        },
        "family": {
            "yearly": 196,
            "oneTime": 30,
            "total": 226
        }
    }, {
        "id": "53",
        "cantonId": "BE",
        "name": "SAC Grindelwald",
        "youth": {
            "yearly": 75,
            "oneTime": 0,
            "total": 75
        },
        "single": {
            "yearly": 120,
            "oneTime": 20,
            "total": 140
        },
        "family": {
            "yearly": 183,
            "oneTime": 30,
            "total": 213
        }
    }, {
        "id": "45",
        "cantonId": "BE",
        "name": "SAC Grossh\u00f6chstetten",
        "youth": {
            "yearly": 48,
            "oneTime": 0,
            "total": 48
        },
        "single": {
            "yearly": 108,
            "oneTime": 20,
            "total": 128
        },
        "family": {
            "yearly": 176,
            "oneTime": 30,
            "total": 206
        }
    }, {
        "id": "56",
        "cantonId": "BL",
        "name": "SAC Hohe Winde",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 135,
            "oneTime": 40,
            "total": 175
        },
        "family": {
            "yearly": 199,
            "oneTime": 50,
            "total": 249
        }
    }, {
        "id": "57",
        "cantonId": "ZH",
        "name": "SAC Hoher Rohn",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 135,
            "oneTime": 40,
            "total": 175
        },
        "family": {
            "yearly": 210,
            "oneTime": 60,
            "total": 270
        }
    }, {
        "id": "59",
        "cantonId": "ZH",
        "name": "SAC H\u00f6rnli",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 123,
            "oneTime": 20,
            "total": 143
        },
        "family": {
            "yearly": 191,
            "oneTime": 30,
            "total": 221
        }
    }, {
        "id": "26",
        "cantonId": "BE",
        "name": "SAC Huttwil",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 113,
            "oneTime": 20,
            "total": 133
        },
        "family": {
            "yearly": 186,
            "oneTime": 30,
            "total": 216
        }
    }, {
        "id": "60",
        "cantonId": "BE",
        "name": "SAC Interlaken",
        "youth": {
            "yearly": 60,
            "oneTime": 5,
            "total": 65
        },
        "single": {
            "yearly": 115,
            "oneTime": 25,
            "total": 140
        },
        "family": {
            "yearly": 172,
            "oneTime": 40,
            "total": 212
        }
    }, {
        "id": "64",
        "cantonId": "FR",
        "name": "SAC Kaiseregg",
        "youth": {
            "yearly": 53,
            "oneTime": 20,
            "total": 73
        },
        "single": {
            "yearly": 108,
            "oneTime": 45,
            "total": 153
        },
        "family": {
            "yearly": 174,
            "oneTime": 65,
            "total": 239
        }
    }, {
        "id": "65",
        "cantonId": "SG",
        "name": "SAC Kamor",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 110,
            "oneTime": 20,
            "total": 130
        },
        "family": {
            "yearly": 160,
            "oneTime": 30,
            "total": 190
        }
    }, {
        "id": "66",
        "cantonId": "BE",
        "name": "SAC Kirchberg",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 115,
            "oneTime": 20,
            "total": 135
        },
        "family": {
            "yearly": 192,
            "oneTime": 30,
            "total": 222
        }
    }, {
        "id": "67",
        "cantonId": "AG",
        "name": "SAC L\u00e4gern",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 140,
            "oneTime": 40,
            "total": 180
        },
        "family": {
            "yearly": 220,
            "oneTime": 60,
            "total": 280
        }
    }, {
        "id": "69",
        "cantonId": "BE",
        "name": "SAC Lauterbrunnen",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 110,
            "oneTime": 40,
            "total": 150
        },
        "family": {
            "yearly": 174,
            "oneTime": 60,
            "total": 234
        }
    }, {
        "id": "70",
        "cantonId": "BE",
        "name": "SAC Ledifluh",
        "youth": {
            "yearly": 48,
            "oneTime": 0,
            "total": 48
        },
        "single": {
            "yearly": 133,
            "oneTime": 30,
            "total": 163
        },
        "family": {
            "yearly": 206,
            "oneTime": 40,
            "total": 246
        }
    }, {
        "id": "72",
        "cantonId": "AG",
        "name": "SAC Lindenberg",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 115,
            "oneTime": 20,
            "total": 135
        },
        "family": {
            "yearly": 182,
            "oneTime": 30,
            "total": 212
        }
    }, {
        "id": "74",
        "cantonId": "ZH",
        "name": "SAC Manegg",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 125,
            "oneTime": 40,
            "total": 165
        },
        "family": {
            "yearly": 210,
            "oneTime": 50,
            "total": 260
        }
    }, {
        "id": "85",
        "cantonId": "VS",
        "name": "SAC Monte Rosa Brig",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "84",
        "cantonId": "VS",
        "name": "SAC Monte Rosa St.Niklaus",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "83",
        "cantonId": "VS",
        "name": "SAC Monte Rosa Visp",
        "youth": {
            "yearly": 47,
            "oneTime": 0,
            "total": 47
        },
        "single": {
            "yearly": 114,
            "oneTime": 30,
            "total": 144
        },
        "family": {
            "yearly": 172,
            "oneTime": 45,
            "total": 217
        }
    }, {
        "id": "16",
        "cantonId": "FR",
        "name": "SAC Murten",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 125,
            "oneTime": 20,
            "total": 145
        },
        "family": {
            "yearly": 188,
            "oneTime": 30,
            "total": 218
        }
    }, {
        "id": "88",
        "cantonId": "SZ",
        "name": "SAC Mythen",
        "youth": {
            "yearly": 40,
            "oneTime": 10,
            "total": 50
        },
        "single": {
            "yearly": 100,
            "oneTime": 30,
            "total": 130
        },
        "family": {
            "yearly": 162,
            "oneTime": 50,
            "total": 212
        }
    }, {
        "id": "90",
        "cantonId": "BE",
        "name": "SAC Niesen",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 100,
            "oneTime": 30,
            "total": 130
        },
        "family": {
            "yearly": 160,
            "oneTime": 40,
            "total": 200
        }
    }, {
        "id": "91",
        "cantonId": "BE",
        "name": "SAC Oberaargau",
        "youth": {
            "yearly": 76,
            "oneTime": 0,
            "total": 76
        },
        "single": {
            "yearly": 131,
            "oneTime": 40,
            "total": 171
        },
        "family": {
            "yearly": 226,
            "oneTime": 60,
            "total": 286
        }
    }, {
        "id": "92",
        "cantonId": "SO",
        "name": "SAC Oberaargau",
        "youth": {
            "yearly": 76,
            "oneTime": 0,
            "total": 76
        },
        "single": {
            "yearly": 131,
            "oneTime": 40,
            "total": 171
        },
        "family": {
            "yearly": 226,
            "oneTime": 60,
            "total": 286
        }
    }, {
        "id": "96",
        "cantonId": "BE",
        "name": "SAC Oberhasli",
        "youth": {
            "yearly": 70,
            "oneTime": 0,
            "total": 70
        },
        "single": {
            "yearly": 107,
            "oneTime": 40,
            "total": 147
        },
        "family": {
            "yearly": 174,
            "oneTime": 50,
            "total": 224
        }
    }, {
        "id": "97",
        "cantonId": "BE",
        "name": "SAC Oldenhorn",
        "youth": {
            "yearly": 52,
            "oneTime": 0,
            "total": 52
        },
        "single": {
            "yearly": 106,
            "oneTime": 20,
            "total": 126
        },
        "family": {
            "yearly": 221,
            "oneTime": 30,
            "total": 251
        }
    }, {
        "id": "98",
        "cantonId": "SO",
        "name": "SAC Olten",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 115,
            "oneTime": 40,
            "total": 155
        },
        "family": {
            "yearly": 190,
            "oneTime": 70,
            "total": 260
        }
    }, {
        "id": "99",
        "cantonId": "ZH",
        "name": "SAC Pfannenstiel",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 130,
            "oneTime": 25,
            "total": 155
        },
        "family": {
            "yearly": 210,
            "oneTime": 40,
            "total": 250
        }
    }, {
        "id": "101",
        "cantonId": "LU",
        "name": "SAC Pilatus",
        "youth": {
            "yearly": 54,
            "oneTime": 0,
            "total": 54
        },
        "single": {
            "yearly": 142,
            "oneTime": 70,
            "total": 212
        },
        "family": {
            "yearly": 233,
            "oneTime": 80,
            "total": 313
        }
    }, {
        "id": "104",
        "cantonId": "LU",
        "name": "SAC Pilatus Hochdorf",
        "youth": {
            "yearly": 54,
            "oneTime": 0,
            "total": 54
        },
        "single": {
            "yearly": 152,
            "oneTime": 70,
            "total": 222
        },
        "family": {
            "yearly": 243,
            "oneTime": 80,
            "total": 323
        }
    }, {
        "id": "103",
        "cantonId": "LU",
        "name": "SAC Pilatus Napf",
        "youth": {
            "yearly": 54,
            "oneTime": 0,
            "total": 54
        },
        "single": {
            "yearly": 142,
            "oneTime": 70,
            "total": 212
        },
        "family": {
            "yearly": 233,
            "oneTime": 80,
            "total": 313
        }
    }, {
        "id": "105",
        "cantonId": "SZ",
        "name": "SAC Pilatus Rigi",
        "youth": {
            "yearly": 54,
            "oneTime": 0,
            "total": 54
        },
        "single": {
            "yearly": 157,
            "oneTime": 70,
            "total": 227
        },
        "family": {
            "yearly": 253,
            "oneTime": 80,
            "total": 333
        }
    }, {
        "id": "102",
        "cantonId": "LU",
        "name": "SAC Pilatus Surental",
        "youth": {
            "yearly": 54,
            "oneTime": 0,
            "total": 54
        },
        "single": {
            "yearly": 142,
            "oneTime": 70,
            "total": 212
        },
        "family": {
            "yearly": 233,
            "oneTime": 80,
            "total": 313
        }
    }, {
        "id": "106",
        "cantonId": "UR",
        "name": "SAC Piz Lucendro",
        "youth": {
            "yearly": 43,
            "oneTime": 0,
            "total": 43
        },
        "single": {
            "yearly": 104,
            "oneTime": 20,
            "total": 124
        },
        "family": {
            "yearly": 176,
            "oneTime": 30,
            "total": 206
        }
    }, {
        "id": "55",
        "cantonId": "GR",
        "name": "SAC Piz Platta",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 113,
            "oneTime": 20,
            "total": 133
        },
        "family": {
            "yearly": 176,
            "oneTime": 30,
            "total": 206
        }
    }, {
        "id": "107",
        "cantonId": "SG",
        "name": "SAC Piz Sol",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 125,
            "oneTime": 40,
            "total": 165
        },
        "family": {
            "yearly": 210,
            "oneTime": 60,
            "total": 270
        }
    }, {
        "id": "108",
        "cantonId": "GR",
        "name": "SAC Piz Terri",
        "youth": {
            "yearly": 45,
            "oneTime": 20,
            "total": 65
        },
        "single": {
            "yearly": 105,
            "oneTime": 40,
            "total": 145
        },
        "family": {
            "yearly": 161,
            "oneTime": 50,
            "total": 211
        }
    }, {
        "id": "109",
        "cantonId": "GR",
        "name": "SAC Pr\u00e4ttigau",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 105,
            "oneTime": 20,
            "total": 125
        },
        "family": {
            "yearly": 165,
            "oneTime": 30,
            "total": 195
        }
    }, {
        "id": "110",
        "cantonId": "BS",
        "name": "SAC Pr\u00e4ttigau Baslerkam.",
        "youth": {
            "yearly": 30,
            "oneTime": 0,
            "total": 30
        },
        "single": {
            "yearly": 103,
            "oneTime": 20,
            "total": 123
        },
        "family": {
            "yearly": 150,
            "oneTime": 30,
            "total": 180
        }
    }, {
        "id": "113",
        "cantonId": "SH",
        "name": "SAC Randen",
        "youth": {
            "yearly": 55,
            "oneTime": 0,
            "total": 55
        },
        "single": {
            "yearly": 123,
            "oneTime": 20,
            "total": 143
        },
        "family": {
            "yearly": 192,
            "oneTime": 30,
            "total": 222
        }
    }, {
        "id": "114",
        "cantonId": "GR",
        "name": "SAC R\u00e4tia",
        "youth": {
            "yearly": 57,
            "oneTime": 0,
            "total": 57
        },
        "single": {
            "yearly": 145,
            "oneTime": 20,
            "total": 165
        },
        "family": {
            "yearly": 205,
            "oneTime": 30,
            "total": 235
        }
    }, {
        "id": "115",
        "cantonId": "SG",
        "name": "SAC Rhein",
        "youth": {
            "yearly": 63,
            "oneTime": 0,
            "total": 63
        },
        "single": {
            "yearly": 108,
            "oneTime": 20,
            "total": 128
        },
        "family": {
            "yearly": 176,
            "oneTime": 30,
            "total": 206
        }
    }, {
        "id": "116",
        "cantonId": "ZH",
        "name": "SAC Rinsberg",
        "youth": {
            "yearly": 78,
            "oneTime": 0,
            "total": 78
        },
        "single": {
            "yearly": 118,
            "oneTime": 20,
            "total": 138
        },
        "family": {
            "yearly": 222,
            "oneTime": 30,
            "total": 252
        }
    }, {
        "id": "117",
        "cantonId": "SG",
        "name": "SAC Rorschach",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 120,
            "oneTime": 20,
            "total": 140
        },
        "family": {
            "yearly": 214,
            "oneTime": 30,
            "total": 244
        }
    }, {
        "id": "118",
        "cantonId": "ZG",
        "name": "SAC Rossberg",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 137,
            "oneTime": 30,
            "total": 167
        },
        "family": {
            "yearly": 207,
            "oneTime": 50,
            "total": 257
        }
    }, {
        "id": "119",
        "cantonId": "VS",
        "name": "SAC Saas",
        "youth": {
            "yearly": 61,
            "oneTime": 0,
            "total": 61
        },
        "single": {
            "yearly": 108,
            "oneTime": 30,
            "total": 138
        },
        "family": {
            "yearly": 161,
            "oneTime": 50,
            "total": 211
        }
    }, {
        "id": "120",
        "cantonId": "AR",
        "name": "SAC S\u00e4ntis",
        "youth": {
            "yearly": 55,
            "oneTime": 20,
            "total": 75
        },
        "single": {
            "yearly": 110,
            "oneTime": 40,
            "total": 150
        },
        "family": {
            "yearly": 180,
            "oneTime": 50,
            "total": 230
        }
    }, {
        "id": "121",
        "cantonId": "BE",
        "name": "SAC Seeland",
        "youth": {
            "yearly": 67,
            "oneTime": 0,
            "total": 67
        },
        "single": {
            "yearly": 120,
            "oneTime": 25,
            "total": 145
        },
        "family": {
            "yearly": 190,
            "oneTime": 35,
            "total": 225
        }
    }, {
        "id": "124",
        "cantonId": "SG",
        "name": "SAC St. Gallen",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 142,
            "oneTime": 20,
            "total": 162
        },
        "family": {
            "yearly": 232,
            "oneTime": 30,
            "total": 262
        }
    }, {
        "id": "125",
        "cantonId": "BE",
        "name": "SAC Stockhorn",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 120,
            "oneTime": 25,
            "total": 145
        },
        "family": {
            "yearly": 190,
            "oneTime": 40,
            "total": 230
        }
    }, {
        "id": "126",
        "cantonId": "TG",
        "name": "SAC Thurgau",
        "youth": {
            "yearly": 51,
            "oneTime": 0,
            "total": 51
        },
        "single": {
            "yearly": 131,
            "oneTime": 25,
            "total": 156
        },
        "family": {
            "yearly": 222,
            "oneTime": 35,
            "total": 257
        }
    }, {
        "id": "128",
        "cantonId": "NW",
        "name": "SAC Titlis",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 115,
            "oneTime": 35,
            "total": 150
        },
        "family": {
            "yearly": 184,
            "oneTime": 45,
            "total": 229
        }
    }, {
        "id": "129",
        "cantonId": "GL",
        "name": "SAC T\u00f6di",
        "youth": {
            "yearly": 55,
            "oneTime": 2,
            "total": 57
        },
        "single": {
            "yearly": 117,
            "oneTime": 22,
            "total": 139
        },
        "family": {
            "yearly": 194,
            "oneTime": 32,
            "total": 226
        }
    }, {
        "id": "130",
        "cantonId": "SG",
        "name": "SAC Toggenburg",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 113,
            "oneTime": 45,
            "total": 158
        },
        "family": {
            "yearly": 162,
            "oneTime": 55,
            "total": 217
        }
    }, {
        "id": "131",
        "cantonId": "ZH",
        "name": "SAC Uto",
        "youth": {
            "yearly": 72,
            "oneTime": 0,
            "total": 72
        },
        "single": {
            "yearly": 140,
            "oneTime": 85,
            "total": 225
        },
        "family": {
            "yearly": 220,
            "oneTime": 140,
            "total": 360
        }
    }, {
        "id": "132",
        "cantonId": "SG",
        "name": "SAC Uzwil",
        "youth": {
            "yearly": 53,
            "oneTime": 0,
            "total": 53
        },
        "single": {
            "yearly": 113,
            "oneTime": 20,
            "total": 133
        },
        "family": {
            "yearly": 208,
            "oneTime": 30,
            "total": 238
        }
    }, {
        "id": "135",
        "cantonId": "SO",
        "name": "SAC Weissenstein",
        "youth": {
            "yearly": 44,
            "oneTime": 0,
            "total": 44
        },
        "single": {
            "yearly": 113,
            "oneTime": 20,
            "total": 133
        },
        "family": {
            "yearly": 167,
            "oneTime": 30,
            "total": 197
        }
    }, {
        "id": "136",
        "cantonId": "BE",
        "name": "SAC Wildhorn",
        "youth": {
            "yearly": 52,
            "oneTime": 0,
            "total": 52
        },
        "single": {
            "yearly": 107,
            "oneTime": 40,
            "total": 147
        },
        "family": {
            "yearly": 174,
            "oneTime": 60,
            "total": 234
        }
    }, {
        "id": "137",
        "cantonId": "BE",
        "name": "SAC Wildstrubel",
        "youth": {
            "yearly": 57,
            "oneTime": 0,
            "total": 57
        },
        "single": {
            "yearly": 107,
            "oneTime": 20,
            "total": 127
        },
        "family": {
            "yearly": 189,
            "oneTime": 30,
            "total": 219
        }
    }, {
        "id": "138",
        "cantonId": "ZH",
        "name": "SAC Winterthur",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 130,
            "oneTime": 20,
            "total": 150
        },
        "family": {
            "yearly": 220,
            "oneTime": 30,
            "total": 250
        }
    }, {
        "id": "140",
        "cantonId": "VS",
        "name": "SAC Zermatt",
        "youth": {
            "yearly": 50,
            "oneTime": 0,
            "total": 50
        },
        "single": {
            "yearly": 98,
            "oneTime": 30,
            "total": 128
        },
        "family": {
            "yearly": 156,
            "oneTime": 50,
            "total": 206
        }
    }, {
        "id": "141",
        "cantonId": "ZH",
        "name": "SAC Zimmerberg",
        "youth": {
            "yearly": 40,
            "oneTime": 0,
            "total": 40
        },
        "single": {
            "yearly": 126,
            "oneTime": 30,
            "total": 156
        },
        "family": {
            "yearly": 202,
            "oneTime": 40,
            "total": 242
        }
    }, {
        "id": "142",
        "cantonId": "SZ",
        "name": "SAC Zindelspitz",
        "youth": {
            "yearly": 65,
            "oneTime": 0,
            "total": 65
        },
        "single": {
            "yearly": 120,
            "oneTime": 20,
            "total": 140
        },
        "family": {
            "yearly": 200,
            "oneTime": 30,
            "total": 230
        }
    }, {
        "id": "143",
        "cantonId": "AG",
        "name": "SAC Zofingen",
        "youth": {
            "yearly": 60,
            "oneTime": 0,
            "total": 60
        },
        "single": {
            "yearly": 127,
            "oneTime": 20,
            "total": 147
        },
        "family": {
            "yearly": 214,
            "oneTime": 30,
            "total": 244
        }
    }]
}