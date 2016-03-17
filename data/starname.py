self.redis.lpush('starname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
self.redis.lpush('starname_shortname_template', '{{params.fullname}}')
self.redis.lpush('starname_formalname_template', '{{params.fullname}}')

SET   starname_post_chance 30

#

self.redis.lpush('starname_pre', 'To')
self.redis.lpush('starname_pre', 'Na')
self.redis.lpush('starname_pre', 'Wo')
self.redis.lpush('starname_pre', 'Me')
self.redis.lpush('starname_pre', 'Si')
self.redis.lpush('starname_pre', 'Lu')
self.redis.lpush('starname_pre', 'Uu')
self.redis.lpush('starname_pre', 'Aba')
self.redis.lpush('starname_pre', 'Be')
self.redis.lpush('starname_pre', 'Ce')
self.redis.lpush('starname_pre', 'Kro')

self.redis.lpush('starname_root', 'r')
self.redis.lpush('starname_root', 'k')
self.redis.lpush('starname_root', 'l')
self.redis.lpush('starname_root', 'j')
self.redis.lpush('starname_root', 'c')
self.redis.lpush('starname_root', 'x')
self.redis.lpush('starname_root', 'n')


self.redis.lpush('starname_post', 'ay')
self.redis.lpush('starname_post', 'us')
self.redis.lpush('starname_post', 'or')
self.redis.lpush('starname_post', 'an')
self.redis.lpush('starname_post', 'el')
self.redis.lpush('starname_post', 'ub')
self.redis.lpush('starname_post', 'uri')
self.redis.lpush('starname_post', 'un')
self.redis.lpush('starname_post', 'ol')
self.redis.lpush('starname_post', 'on')

# Common star names; parse these into pieces.
#ACAMAR
#ACHERNAR
#Achird
#ACRUX
#Acubens
#ADARA
#Adhafera
#Adhil
#AGENA
#Ain al Rami
#Ain
#Al Anz
#Al Kalb al Rai
#Al Minliar al Asad
#Al Minliar al Shuja
#Aladfar
#Alathfar
#Albaldah
#Albali
#ALBIREO
#Alchiba
#ALCOR
#ALCYONE
#ALDEBARAN
#ALDERAMIN
#Aldhibah
#Alfecca Meridiana
#Alfirk
#ALGENIB
#ALGIEBA
#ALGOL
#Algorab
#ALHENA
#ALIOTH
#ALKAID
#Alkalurops
#Alkes
#Alkurhah
#ALMAAK
#ALNAIR
#ALNATH
#ALNILAM
#ALNITAK
#Alniyat
#Alniyat
#ALPHARD
#ALPHEKKA
#ALPHERATZ
#Alrai
#Alrisha
#Alsafi
#Alsciaukat
#ALSHAIN
#Alshat
#Alsuhail
#ALTAIR
#Altarf
#Alterf
#Aludra
#Alula Australis
#Alula Borealis
#Alya
#Alzirr
#Ancha
#Angetenar
#ANKAA
#Anser
#ANTARES
#ARCTURUS
#Arkab Posterior
#Arkab Prior
#ARNEB
#Arrakis
#Ascella
#Asellus Australis
#Asellus Borealis
#Asellus Primus
#Asellus Secondus
#Asellus Tertius
#Asterope
#Atik
#Atlas
#Auva
#Avior
#Azelfafage
#Azha
#Azmidiske
#Baham
#Baten Kaitos
#Becrux
#Beid
#BELLATRIX
#BETELGEUSE
#Botein
#Brachium
#CANOPUS
#CAPELLA
#Caph
#CASTOR
#Cebalrai
#Celaeno
#Chara
#Chort
#COR CAROLI
#Cursa
#Dabih
#Deneb Algedi
#Deneb Dulfim
#Deneb el Okab
#Deneb el Okab
#Deneb Kaitos Shemali
#DENEB
#DENEBOLA
#Dheneb
#Diadem
#DIPHDA
#Double Double (7051)
#Double Double (7052)
#Double Double (7053)
#Double Double (7054)
#Dschubba
#Dsiban
#DUBHE
#Ed Asich
#Electra
#ELNATH
#ENIF
#ETAMIN
#FOMALHAUT
#Fornacis
#Fum al Samakah
#Furud
#Gacrux
#Gianfar
#Gienah Cygni
#Gienah Ghurab
#Gomeisa
#Gorgonea Quarta
#Gorgonea Secunda
#Gorgonea Tertia
#Graffias
#Grafias
#Grumium
#HADAR
#Haedi
#HAMAL
#Hassaleh
#Head of Hydrus
#Herschel\'s "Garnet Star"
#Heze
#Hoedus II
#Homam
#Hyadum I
#Hyadum II
#IZAR
#Jabbah
#Kaffaljidhma
#Kajam
#KAUS AUSTRALIS
#Kaus Borealis
#Kaus Meridionalis
#Keid
#Kitalpha
#KOCAB
#Kornephoros
#Kraz
#Kuma
#Lesath
#Maasym
#Maia
#Marfak
#Marfak
#Marfic
#Marfik
#MARKAB
#Matar
#Mebsuta
#MEGREZ
#Meissa
#Mekbuda
#Menkalinan
#MENKAR
#Menkar
#Menkent
#Menkib
#MERAK
#Merga
#Merope
#Mesarthim
#Metallah
#Miaplacidus
#Minkar
#MINTAKA
#MIRA
#MIRACH
#Miram
#MIRPHAK
#MIZAR
#Mufrid
#Muliphen
#Murzim
#Muscida
#Muscida
#Muscida
#Nair al Saif
#Naos
#Nash
#Nashira
#Nekkar
#NIHAL
#Nodus Secundus
#NUNKI
#Nusakan
#Peacock
#PHAD
#Phaet
#Pherkad Minor
#Pherkad
#Pleione
#Polaris Australis
#POLARIS
#POLLUX
#Porrima
#Praecipua
#Prima Giedi
#PROCYON
#Propus
#Propus
#Propus
#Rana
#Ras Elased Australis
#Ras Elased Borealis
#RASALGETHI
#RASALHAGUE
#Rastaban
#REGULUS
#Rigel Kentaurus
#RIGEL
#Rijl al Awwa
#Rotanev
#Ruchba
#Ruchbah
#Rukbat
#Sabik
#Sadalachbia
#SADALMELIK
#Sadalsuud
#Sadr
#SAIPH
#Salm
#Sargas
#Sarin
#Sceptrum
#SCHEAT
#Secunda Giedi
#Segin
#Seginus
#Sham
#Sharatan
#SHAULA
#SHEDIR
#Sheliak
#SIRIUS
#Situla
#Skat
#SPICA
#Sterope II
#Sualocin
#Subra
#Suhail al Muhlif
#Sulafat
#Syrma
#Tabit (1543)
#Tabit (1544)
#Tabit (1552)
#Tabit (1570)
#Talitha
#Tania Australis
#Tania Borealis
#TARAZED
#Taygeta
#Tegmen
#Tejat Posterior
#Terebellum
#Terebellum
#Terebellum
#Terebellum
#Thabit
#Theemim
#THUBAN
#Torcularis Septentrionalis
#Turais
#Tyl
#UNUKALHAI
#VEGA
#VINDEMIATRIX
#Wasat
#Wezen
#Wezn
#Yed Posterior
#Yed Prior
#Yildun
#Zaniah
#Zaurak
#Zavijah
#Zibal
#Zosma
#Zuben Elakrab
#Zuben Elakribi
#Zuben Elgenubi
#Zuben Elschemali
