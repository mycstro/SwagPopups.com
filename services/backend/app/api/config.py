# config.py

import os

class BaseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentBaseConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")

class Config:
    """
    Base configuration class shared by all environments.
    """
    SECRET_KEY = 'your_secret_key_here'  # Example secret key for development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///membership.db'  # Example local database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Common settings can go here

class DevelopmentConfig(Config):
    """
    Configuration for development.
    Debug mode, local database, etc.
    """
    DEBUG = True
    #SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///membership.db'  # Example local database
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    MOCK_USERS = {
        "vendor@example.com": {"username": "VendorUser", "is_vendor": True},
        "customer@example.com": {"username": "CustomerUser", "is_vendor": False},
        "mycstro@yahoo.com": {"username": "Mycstro", "is_vendor": True}
    } 
    COUNTRYCODES = [
    ('+1', 'United States (+1)'),
    ('+93', 'Afghanistan (+93)'),
    ('+355', 'Albania (+355)'),
    ('+213', 'Algeria (+213)'),
    ('+1-684', 'American Samoa (+1-684)'),
    ('+376', 'Andorra (+376)'),
    ('+244', 'Angola (+244)'),
    ('+1-264', 'Anguilla (+1-264)'),
    ('+672', 'Antarctica (+672)'),
    ('+1-268', 'Antigua and Barbuda (+1-268)'),
    ('+54', 'Argentina (+54)'),
    ('+374', 'Armenia (+374)'),
    ('+297', 'Aruba (+297)'),
    ('+61', 'Australia (+61)'),
    ('+43', 'Austria (+43)'),
    ('+994', 'Azerbaijan (+994)'),
    ('+1-242', 'Bahamas (+1-242)'),
    ('+973', 'Bahrain (+973)'),
    ('+880', 'Bangladesh (+880)'),
    ('+1-246', 'Barbados (+1-246)'),
    ('+375', 'Belarus (+375)'),
    ('+32', 'Belgium (+32)'),
    ('+501', 'Belize (+501)'),
    ('+229', 'Benin (+229)'),
    ('+1-441', 'Bermuda (+1-441)'),
    ('+975', 'Bhutan (+975)'),
    ('+591', 'Bolivia (+591)'),
    ('+387', 'Bosnia and Herzegovina (+387)'),
    ('+267', 'Botswana (+267)'),
    ('+55', 'Brazil (+55)'),
    ('+246', 'British Indian Ocean Territory (+246)'),
    ('+1-284', 'British Virgin Islands (+1-284)'),
    ('+673', 'Brunei (+673)'),
    ('+359', 'Bulgaria (+359)'),
    ('+226', 'Burkina Faso (+226)'),
    ('+257', 'Burundi (+257)'),
    ('+855', 'Cambodia (+855)'),
    ('+237', 'Cameroon (+237)'),
    ('+1', 'Canada (+1)'),
    ('+238', 'Cape Verde (+238)'),
    ('+1-345', 'Cayman Islands (+1-345)'),
    ('+236', 'Central African Republic (+236)'),
    ('+235', 'Chad (+235)'),
    ('+56', 'Chile (+56)'),
    ('+86', 'China (+86)'),
    ('+61', 'Christmas Island (+61)'),
    ('+61', 'Cocos (Keeling) Islands (+61)'),
    ('+57', 'Colombia (+57)'),
    ('+269', 'Comoros (+269)'),
    ('+682', 'Cook Islands (+682)'),
    ('+506', 'Costa Rica (+506)'),
    ('+385', 'Croatia (+385)'),
    ('+53', 'Cuba (+53)'),
    ('+599', 'Curaçao (+599)'),
    ('+357', 'Cyprus (+357)'),
    ('+420', 'Czech Republic (+420)'),
    ('+243', 'Democratic Republic of the Congo (+243)'),
    ('+45', 'Denmark (+45)'),
    ('+253', 'Djibouti (+253)'),
    ('+1-767', 'Dominica (+1-767)'),
    ('+1-809', 'Dominican Republic (+1-809)'),
    ('+593', 'Ecuador (+593)'),
    ('+20', 'Egypt (+20)'),
    ('+503', 'El Salvador (+503)'),
    ('+240', 'Equatorial Guinea (+240)'),
    ('+291', 'Eritrea (+291)'),
    ('+372', 'Estonia (+372)'),
    ('+251', 'Ethiopia (+251)'),
    ('+500', 'Falkland Islands (+500)'),
    ('+298', 'Faroe Islands (+298)'),
    ('+679', 'Fiji (+679)'),
    ('+358', 'Finland (+358)'),
    ('+33', 'France (+33)'),
    ('+689', 'French Polynesia (+689)'),
    ('+241', 'Gabon (+241)'),
    ('+220', 'Gambia (+220)'),
    ('+995', 'Georgia (+995)'),
    ('+49', 'Germany (+49)'),
    ('+233', 'Ghana (+233)'),
    ('+350', 'Gibraltar (+350)'),
    ('+30', 'Greece (+30)'),
    ('+299', 'Greenland (+299)'),
    ('+1-473', 'Grenada (+1-473)'),
    ('+1-671', 'Guam (+1-671)'),
    ('+502', 'Guatemala (+502)'),
    ('+44-1481', 'Guernsey (+44-1481)'),
    ('+224', 'Guinea (+224)'),
    ('+245', 'Guinea-Bissau (+245)'),
    ('+592', 'Guyana (+592)'),
    ('+509', 'Haiti (+509)'),
    ('+504', 'Honduras (+504)'),
    ('+852', 'Hong Kong (+852)'),
    ('+36', 'Hungary (+36)'),
    ('+354', 'Iceland (+354)'),
    ('+91', 'India (+91)'),
    ('+62', 'Indonesia (+62)'),
    ('+98', 'Iran (+98)'),
    ('+964', 'Iraq (+964)'),
    ('+353', 'Ireland (+353)'),
    ('+44-1624', 'Isle of Man (+44-1624)'),
    ('+972', 'Israel (+972)'),
    ('+39', 'Italy (+39)'),
    ('+225', 'Ivory Coast (+225)'),
    ('+1-876', 'Jamaica (+1-876)'),
    ('+81', 'Japan (+81)'),
    ('+44-1534', 'Jersey (+44-1534)'),
    ('+962', 'Jordan (+962)'),
    ('+7', 'Kazakhstan (+7)'),
    ('+254', 'Kenya (+254)'),
    ('+686', 'Kiribati (+686)'),
    ('+383', 'Kosovo (+383)'),
    ('+965', 'Kuwait (+965)'),
    ('+996', 'Kyrgyzstan (+996)'),
    ('+856', 'Laos (+856)'),
    ('+371', 'Latvia (+371)'),
    ('+961', 'Lebanon (+961)'),
    ('+266', 'Lesotho (+266)'),
    ('+231', 'Liberia (+231)'),
    ('+218', 'Libya (+218)'),
    ('+423', 'Liechtenstein (+423)'),
    ('+370', 'Lithuania (+370)'),
    ('+352', 'Luxembourg (+352)'),
    ('+853', 'Macau (+853)'),
    ('+389', 'Macedonia (+389)'),
    ('+261', 'Madagascar (+261)'),
    ('+265', 'Malawi (+265)'),
    ('+60', 'Malaysia (+60)'),
    ('+960', 'Maldives (+960)'),
    ('+223', 'Mali (+223)'),
    ('+356', 'Malta (+356)'),
    ('+692', 'Marshall Islands (+692)'),
    ('+222', 'Mauritania (+222)'),
    ('+230', 'Mauritius (+230)'),
    ('+262', 'Mayotte (+262)'),
    ('+52', 'Mexico (+52)'),
    ('+691', 'Micronesia (+691)'),
    ('+373', 'Moldova (+373)'),
    ('+377', 'Monaco (+377)'),
    ('+976', 'Mongolia (+976)'),
    ('+382', 'Montenegro (+382)'),
    ('+1-664', 'Montserrat (+1-664)'),
    ('+212', 'Morocco (+212)'),
    ('+258', 'Mozambique (+258)'),
    ('+95', 'Myanmar (+95)'),
    ('+264', 'Namibia (+264)'),
    ('+674', 'Nauru (+674)'),
    ('+977', 'Nepal (+977)'),
    ('+31', 'Netherlands (+31)'),
    ('+599', 'Netherlands Antilles (+599)'),
    ('+687', 'New Caledonia (+687)'),
    ('+64', 'New Zealand (+64)'),
    ('+505', 'Nicaragua (+505)'),
    ('+227', 'Niger (+227)'),
    ('+234', 'Nigeria (+234)'),
    ('+683', 'Niue (+683)'),
    ('+850', 'North Korea (+850)'),
    ('+1-670', 'Northern Mariana Islands (+1-670)'),
    ('+47', 'Norway (+47)'),
    ('+968', 'Oman (+968)'),
    ('+92', 'Pakistan (+92)'),
    ('+680', 'Palau (+680)'),
    ('+970', 'Palestine (+970)'),
    ('+507', 'Panama (+507)'),
    ('+675', 'Papua New Guinea (+675)'),
    ('+595', 'Paraguay (+595)'),
    ('+51', 'Peru (+51)'),
    ('+63', 'Philippines (+63)'),
    ('+64', 'Pitcairn (+64)'),
    ('+48', 'Poland (+48)'),
    ('+351', 'Portugal (+351)'),
    ('+1-787', 'Puerto Rico (+1-787)'),
    ('+974', 'Qatar (+974)'),
    ('+242', 'Republic of the Congo (+242)'),
    ('+262', 'Reunion (+262)'),
    ('+40', 'Romania (+40)'),
    ('+7', 'Russia (+7)'),
    ('+250', 'Rwanda (+250)'),
    ('+590', 'Saint Barthelemy (+590)'),
    ('+290', 'Saint Helena (+290)'),
    ('+1-869', 'Saint Kitts and Nevis (+1-869)'),
    ('+1-758', 'Saint Lucia (+1-758)'),
    ('+590', 'Saint Martin (+590)'),
    ('+508', 'Saint Pierre and Miquelon (+508)'),
    ('+1-784', 'Saint Vincent and the Grenadines (+1-784)'),
    ('+685', 'Samoa (+685)'),
    ('+378', 'San Marino (+378)'),
    ('+239', 'Sao Tome and Principe (+239)'),
    ('+966', 'Saudi Arabia (+966)'),
    ('+221', 'Senegal (+221)'),
    ('+381', 'Serbia (+381)'),
    ('+248', 'Seychelles (+248)'),
    ('+232', 'Sierra Leone (+232)'),
    ('+65', 'Singapore (+65)'),
    ('+1-721', 'Sint Maarten (+1-721)'),
    ('+421', 'Slovakia (+421)'),
    ('+386', 'Slovenia (+386)'),
    ('+677', 'Solomon Islands (+677)'),
    ('+252', 'Somalia (+252)'),
    ('+27', 'South Africa (+27)'),
    ('+82', 'South Korea (+82)'),
    ('+211', 'South Sudan (+211)'),
    ('+34', 'Spain (+34)'),
    ('+94', 'Sri Lanka (+94)'),
    ('+249', 'Sudan (+249)'),
    ('+597', 'Suriname (+597)'),
    ('+47', 'Svalbard and Jan Mayen (+47)'),
    ('+268', 'Swaziland (Eswatini) (+268)'),
    ('+46', 'Sweden (+46)'),
    ('+41', 'Switzerland (+41)'),
    ('+963', 'Syria (+963)'),
    ('+886', 'Taiwan (+886)'),
    ('+992', 'Tajikistan (+992)'),
    ('+255', 'Tanzania (+255)'),
    ('+66', 'Thailand (+66)'),
    ('+670', 'Timor-Leste (+670)'),
    ('+228', 'Togo (+228)'),
    ('+690', 'Tokelau (+690)'),
    ('+676', 'Tonga (+676)'),
    ('+1-868', 'Trinidad and Tobago (+1-868)'),
    ('+216', 'Tunisia (+216)'),
    ('+90', 'Turkey (+90)'),
    ('+993', 'Turkmenistan (+993)'),
    ('+1-649', 'Turks and Caicos Islands (+1-649)'),
    ('+688', 'Tuvalu (+688)'),
    ('+1-340', 'U.S. Virgin Islands (+1-340)'),
    ('+256', 'Uganda (+256)'),
    ('+380', 'Ukraine (+380)'),
    ('+971', 'United Arab Emirates (+971)'),
    ('+44', 'United Kingdom (+44)'),
    ('+598', 'Uruguay (+598)'),
    ('+998', 'Uzbekistan (+998)'),
    ('+678', 'Vanuatu (+678)'),
    ('+379', 'Vatican City (+379)'),
    ('+58', 'Venezuela (+58)'),
    ('+84', 'Vietnam (+84)'),
    ('+681', 'Wallis and Futuna (+681)'),
    ('+212', 'Western Sahara (+212)'),
    ('+967', 'Yemen (+967)'),
    ('+260', 'Zambia (+260)'),
    ('+263', 'Zimbabwe (+263)')
]

    # A list of USA area codes (as per the North American Numbering Plan).
    # Note: This list is accurate as of the time of writing but may need updates in the future.
    AREA_CODES_BY_LOCATION = {
        "New York City": [
            ("212", "212 - Manhattan"),
            ("347", "347 - NYC Overlay"),
            ("646", "646 - NYC Overlay"),
            ("718", "718 - Outer Boroughs"),
            ("929", "929 - NYC Overlay")
        ],
        "New York": [
            ("518", "518 - New York (Albany/Capital District)"),
            ("607", "607 - New York (Binghamton)"),
            ("917", "917 - New York (Buffalo)"),
            ("918", "918 - New York (Rochester)"),
            ("919", "919 - New York (Syracuse)"),
            ("925", "925 - New York (Yonkers)")
        ],
        "Los Angeles": [
            ("213", "213 - Los Angeles"),
            ("310", "310 - West LA"),
            ("424", "424 - LA Overlay")
        ],
        "Chicago": [
            ("312", "312 - Chicago"),
            ("773", "773 - Chicago"),
            ("872", "872 - Chicago Overlay")
        ],
        "Houston": [
            ("281", "281 - Houston"),
            ("346", "346 - Houston Overlay"),
            ("713", "713 - Houston")
        ],
        "Philadelphia": [
            ("215", "215 - Philadelphia"),
            ("267", "267 - Philadelphia Overlay")
        ],
        "San Francisco Bay Area": [
            ("415", "415 - San Francisco"),
            ("628", "628 - SF Overlay")
        ],
        "Dallas/Fort Worth": [
            ("214", "214 - Dallas"),
            ("972", "972 - DFW Overlay")
        ],
        "Atlanta": [
            ("404", "404 - Atlanta"),
            ("470", "470 - Atlanta Overlay"),
            ("678", "678 - Atlanta Overlay"),
            ("770", "770 - Atlanta Suburbs")
        ],
        "Washington DC": [
            ("202", "202 - Washington, DC")
        ],
        "Miami": [
            ("305", "305 - Miami"),
            ("786", "786 - Miami Overlay")
        ],
        "Boston": [
            ("617", "617 - Boston"),
            ("781", "781 - Boston Suburbs")
        ],
        "Seattle": [
            ("206", "206 - Seattle"),
            ("425", "425 - Seattle Overlay"),
            ("509", "509 - Seattle Suburbs")
        ],
        "San Antonio": [
            ("210", "210 - San Antonio"),
            ("283", "283 - San Antonio Overlay")
        ],
        "San Diego": [
            ("207", "207 - San Diego"),
            ("661", "661 - San Diego Overlay"),
            ("720", "720 - San Diego Overlay"),
            ("760", "760 - San Diego Suburbs"),
            ("750", "750 - San Diego Suburbs"),
            ("775", "775 - San Diego Suburbs"),
            ("770", "770 - San Diego Suburbs")
        ],
        "San Jose": [
            ("408", "408 - San Jose"),
            ("650", "650 - San Jose Overlay"),
            ("714", "714 - San Jose Suburbs")
        ],
        "Other Northeast": [
            ("203", "203 - Connecticut (Bridgeport, New Haven)"),
            ("860", "860 - Connecticut (New Haven area)"),
            ("207", "207 - Maine"),
            ("603", "603 - New Hampshire"),
            ("802", "802 - Vermont")
        ],
        "Other Midwest": [
            ("216", "216 - Cleveland, OH"),
            ("330", "330 - Akron, OH"),
            ("440", "440 - Cleveland Suburbs, OH"),
            ("419", "419 - Toledo, OH"),
            ("513", "513 - Cincinnati, OH"),
            ("614", "614 - Columbus, OH"),
            ("414", "414 - Milwaukee, WI"),
            ("262", "262 - Milwaukee Suburbs, WI")
        ],
        "Other South": [
            ("229", "229 - Albany, GA"),
            ("912", "912 - Savannah, GA"),
            ("251", "251 - Mobile, AL"),
            ("205", "205 - Birmingham, AL"),
            ("334", "334 - Montgomery, AL"),
            ("256", "256 - Huntsville, AL"),
            ("504", "504 - New Orleans, LA"),
            ("318", "318 - Northern Louisiana")
        ],
        "Other West": [
            ("206", "206 - Seattle, WA"),
            ("253", "253 - Tacoma, WA"),
            ("360", "360 - Western WA"),
            ("425", "425 - Seattle Suburbs"),
            ("509", "509 - Eastern WA"),
            ("602", "602 - Phoenix, AZ"),
            ("480", "480 - Mesa/Scottsdale, AZ"),
            ("520", "520 - Tucson, AZ"),
            ("623", "623 - Phoenix Suburbs, AZ"),
            ("928", "928 - Northern AZ"),
            ("303", "303 - Denver, CO"),
            ("720", "720 - Denver Overlay, CO")
        ],
        "Other Southwest": [
            ("210", "210 - San Antonio, TX"),
            ("512", "512 - Austin, TX"),
            ("817", "817 - Fort Worth, TX"),
            ("682", "682 - Fort Worth Overlay, TX")
        ]
    }

    #AREACODES = [
    #    (location, codes) for location, codes in AREA_CODES_BY_LOCATION.items()
    #]

        # Complete list of U.S. states as (abbreviation, full name) tuples.
    USSTATES = [
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming")
    ]

class ProductionConfig(Config):
    """
    Configuration for production.
    Production DB URIs, no debug mode, etc.
    """
    DEBUG = False
    # Example production DB:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@hostname/dbname'
