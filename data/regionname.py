self.redis.lpush('regionname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
self.redis.lpush('regionname_shortname_template', '{{params.fullname}}')
self.redis.lpush('regionname_formalname_template', '{{params.fullname}}')


SET   regionname_title_chance 22
SET   regionname_post_chance 40
SET   regionname_trailer_chance 50



self.redis.lpush('regionname_title', 'East')
self.redis.lpush('regionname_title', 'West')
self.redis.lpush('regionname_title', 'North')
self.redis.lpush('regionname_title', 'South')
self.redis.lpush('regionname_title', 'Lower')
self.redis.lpush('regionname_title', 'Upper')
self.redis.lpush('regionname_title', 'New')

self.redis.lpush('regionname_pre', 'Ab')
self.redis.lpush('regionname_pre', 'Ac')
self.redis.lpush('regionname_pre', 'Ad')
self.redis.lpush('regionname_pre', 'Af')
self.redis.lpush('regionname_pre', 'Ba')
self.redis.lpush('regionname_pre', 'Bi')
self.redis.lpush('regionname_pre', 'Alb')
self.redis.lpush('regionname_pre', 'Lom')
self.redis.lpush('regionname_pre', 'Loir')
self.redis.lpush('regionname_pre', 'Mid')
self.redis.lpush('regionname_pre', 'Pyr')


self.redis.lpush('regionname_root', 'ad')
self.redis.lpush('regionname_root', 'am')
self.redis.lpush('regionname_root', 'bar')
self.redis.lpush('regionname_root', 'ed')
self.redis.lpush('regionname_root', 'har')
self.redis.lpush('regionname_root', 'ja')
self.redis.lpush('regionname_root', 'ruz')

self.redis.lpush('regionname_post', 'a')
self.redis.lpush('regionname_post', 'ad')
self.redis.lpush('regionname_post', 'ain')
self.redis.lpush('regionname_post', 'awa')
self.redis.lpush('regionname_post', 'dy')
self.redis.lpush('regionname_post', 'ia')
self.redis.lpush('regionname_post', 're')
self.redis.lpush('regionname_post', 'zo')


self.redis.lpush('regionname_trailer', 'District')
self.redis.lpush('regionname_trailer', 'Province')
self.redis.lpush('regionname_trailer', 'Region')
self.redis.lpush('regionname_trailer', 'Territory')



#Pays-de-la-Loire
#Basque Country
#Lorraine
#Colima
#Los
#Kebbi
#Nagaland
#Madhya
#Sabah
#Delaware
#Greater Poland
#Cantabria
#Jalisco
#Ayacucho
#Hidalgo
#Valencian Community
#São
#norfolk
#Red Ruthenia
#Oregon
#Zamfara
#Brittany
#Ogun
#Quintana
#Odisha
#Benue
#Centre
#Jammu
#Nuevo
#Falcón
#Yucatán
#Umbria
#Amazonas
#Coahuila
#Champagne-Ardenne
#Florida
#Espírito
#Italian
#Uttar
#Terengganu
#Guerrero
#Aquitaine
#Portuguesa
#Auvergne
#Alabama
#Silesia
#Masovia
#queensland
#Oaxaca
#Calabria
#Durango
#wales
#Morros
#Provence-Alpes-Côte
#Illinois
#Táchira
#Martinique
#Pennsylvania[E]
#West
#Tyrol
#Nova Scotia
#Rhine-Westphalia
#Yobe
#Murcia
#Réunion
#Tabasco
#Andalusia
#Zulia
#San
#Indiana
#Alberta
#Imo
#Veracruz
#Virginia[G]
#Pará
#Louisiana
#Aragon
#Extremadura
#Miranda
#Arizona
#Nebraska
#Puebla
#Mecklenburg-Western
#Madrid
#Balearic Islands
#Monagas
#South Dakota
#Wappen
#Escudo
#Aguascalientes
#Rajasthan
#Southern Podlasie
#Piedmont
#Juan
#Kuyavia
#Guanajuato
#Barinas
#Kerala
#Podlaskie
#Burgundy
#Ebonyi
#British Columbia
#Campania
#Navarra
#Sarawak
#Anzoátegui
#Uttarakhand
#Barquisimeto
#Georgia
#Rhône-Alpes
#Tripura
#Sergipe
#Zacatecas
#Lazio
#Prince Edward Island
#jervis
#Ohio
#Michigan
#amapa
#Westphalia
#Kedah
#Apulia
#Kaduna
#Colorado
#Perak
#North Carolina
#Tennessee
#Kelantan
#Maryland
#Niger
#Mississippi
#Edo
#Malacca
#Ceará
#Sicilian
#Rhineland-Palatinate
#Goiás
#New Brunswick
#Berlin
#ESCUDO
#Catalonia
#Amacuro
#Maracay
#Anambra
#Arunachal
#Coat
#Ontario
#Gombe
#Osun
#Akwa
#Newfoundland and Labrador
#Messina
#Poitou-Charentes
#Distrito
#Wisconsin
#Nevada
#Taraba
#Assam
#Santa
#Giulia
#Bolívar
#Massachusetts[D]
#Missouri
#Chiapas
#Guadeloupe
#Molise
#Guayana
#Castilla y Leon
#Nunavut
#Bahia
#Manipur
#Plateau
#Negeri
#Asturias
#Katsina
#Languedoc-Roussillon
#Maharashtra
#Johor
#Borno
#Nueva
#Utah
#Guárico
#Kansas
#Paraíba
#Tlaxcala
#Kwara
#Apure
#Wyoming
#Enugu
#Haryana
#Limousin
#Lusatia
#Jigawa
#Saskatchewan
#Nord-Pas-de-Calais
#Mérida
#Perlis
#den-Württemberg
#New Jersey
#California
#Bremen
#Bauchi
#Idaho
#Palermo
#Jharkhand
#Texas
#Connecticut
#Valencia
#Kogi
#Prussia
#Mato
#victoria
#Yukon
#Lagos
#amazonas
#Trujillo
#Picardy
#Kano
#New Hampshire
#Canary Islands
#Karnataka
#Franche-Comté
#Ekiti
#Baden-Württemberg
#Bavaria
#North Dakota
#Alaska
#Oklahoma
#West Virginia
#Carabobo
#Barcelona
#Arkansas
#Sokoto
#Himachal
#Île-de-France
#Iowa
#Minnesota
#New Mexico
#Piauí
#Ondo
#Bayelsa
#Quebec
#Paraná
#Tucupita
#Pernambuco
#Sonora
#Nayarit
#Tuscany
#Vermont
#Montana
#Maine
#Marche
#Goa
#Brandenburg
#La Rioja
#Lara
#Rhode Island[F]
#tasmania
#New York
#Basilicata
#Galicia
#Puerto
#Lower
#Liguria
#Kentucky[C]
#alagoas
#Roraima
#Delta
#Selangor
#Tamaulipas
#Northwest Territories
#Pomerania
#Chhattisgarh
#Punjab
#Castilla-La Mancha
#Maranhão
#Ignacio
#Hawaii
#Pomerelia
#Michoacán
#Veneto
#Washington
#Fernando
#Querétaro
#Landessymbol
#Coro
#Upper
#South Carolina
#Saxony
#Nasarawa
#Minas
#Hamburg
#Hesse
#Oyo
#México
#Ciudad
#Corsica
#Pahang
#Meghalaya
#Ibom
#Penang
#Tocantins
#Manitoba
#Campeche
#Sikkim
#Mizoram
#Aragua
#Rondônia
#Alsace
#Andhra
#Emilia-Romagna
#Guiana
#Morelos
#Tamil
#Chihuahua
#Sinaloa
#Gujarat
#Lesser Poland
#
