
########################################################
self.redis.lpush('business_kind', 'bus_adventurersguild')
SET   bus_adventurersguild_kindname adventurers guild
SET   bus_adventurersguild_perbuilding 30
SET   bus_adventurersguild_maxfloors 2
SET   bus_adventurersguild_district professional
self.redis.lpush('bus_adventurersguild_manager', 'adventurer')
self.redis.lpush('bus_adventurersguild_manager', 'mercenary')

self.redis.lpush('bus_adventurersguild_managerclass', 'expert')
self.redis.lpush('bus_adventurersguild_managerclass', 'warrior')
self.redis.lpush('bus_adventurersguild_managerclass', 'rogue')
self.redis.lpush('bus_adventurersguild_managerclass', 'barbarian')
self.redis.lpush('bus_adventurersguild_managerclass', 'bard')
self.redis.lpush('bus_adventurersguild_managerclass', 'fighter')
self.redis.lpush('bus_adventurersguild_managerclass', 'sorcerer')
self.redis.lpush('bus_adventurersguild_managerclass', 'wizard')
self.redis.lpush('bus_adventurersguild_managerclass', 'ranger')

self.redis.lpush('bus_adventurersguild_service', 'contracts')
self.redis.lpush('bus_adventurersguild_service', 'protection')
self.redis.lpush('bus_adventurersguild_service', 'assistance with minor problems')

self.redis.lpush('bus_adventurersguild_trailer', 'hall')
self.redis.lpush('bus_adventurersguild_trailer', 'security')
self.redis.lpush('bus_adventurersguild_trailer', 'legion')
self.redis.lpush('bus_adventurersguild_trailer', 'of hell')
self.redis.lpush('bus_adventurersguild_trailer', 'mercenary')
self.redis.lpush('bus_adventurersguild_trailer', 'union #101')

self.redis.lpush('bus_adventurersguild_smell', 'scent of oil')
self.redis.lpush('bus_adventurersguild_smell', 'smell of blood')
self.redis.lpush('bus_adventurersguild_smell', 'weapons being sharpened')
self.redis.lpush('bus_adventurersguild_smell', 'burning coals')
self.redis.lpush('bus_adventurersguild_smell', 'damp earth')

self.redis.lpush('bus_adventurersguild_sound', 'a dog barking')
self.redis.lpush('bus_adventurersguild_sound', 'sound of sparring')
self.redis.lpush('bus_adventurersguild_sound', 'people yelling')
self.redis.lpush('bus_adventurersguild_sound', 'weapons being sharpened')

self.redis.lpush('bus_adventurersguild_sight', 'weapons against the wall')
self.redis.lpush('bus_adventurersguild_sight', 'equipment lying around')
self.redis.lpush('bus_adventurersguild_sight', 'a still dripping tarp in the corner covering something')

########################################################
self.redis.lpush('business_kind', 'bus_alchemyshop')
SET   bus_alchemyshop_kindname alchemy shop
SET   bus_alchemyshop_perbuilding 3

SET   bus_alchemyshop_maxfloors 1
SET   bus_alchemyshop_district shops

self.redis.lpush('bus_alchemyshop_manager', 'alchemist')

self.redis.lpush('bus_alchemyshop_managerclass', 'expert')
self.redis.lpush('bus_alchemyshop_managerclass', 'adept')
self.redis.lpush('bus_alchemyshop_managerclass', 'sorcerer')
self.redis.lpush('bus_alchemyshop_managerclass', 'wizard')
self.redis.lpush('bus_alchemyshop_managerclass', 'aristocrat')

self.redis.lpush('bus_alchemyshop_service', 'concoctions')
self.redis.lpush('bus_alchemyshop_service', 'service')

self.redis.lpush('bus_alchemyshop_trailer', 'shop')
self.redis.lpush('bus_alchemyshop_trailer', 'shoppe')
self.redis.lpush('bus_alchemyshop_trailer', 'enchanters')

self.redis.lpush('bus_alchemyshop_smell', 'burning coals')
self.redis.lpush('bus_alchemyshop_smell', 'damp earth')
self.redis.lpush('bus_alchemyshop_smell', 'a foul smell')

self.redis.lpush('bus_alchemyshop_sound', 'a dog barking')
self.redis.lpush('bus_alchemyshop_sound', 'a rhythmic scraping')
self.redis.lpush('bus_alchemyshop_sound', 'silence')

self.redis.lpush('bus_alchemyshop_sight', 'a two headed chicken wandering around')
self.redis.lpush('bus_alchemyshop_sight', 'strange bottles and tubes everywhere')
self.redis.lpush('bus_alchemyshop_sight', 'odd smoke coming from a large vat with')

########################################################
self.redis.lpush('business_kind', 'bus_apothecary')
SET   bus_apothecary_kindname apothecary
SET   bus_apothecary_perbuilding 4

SET   bus_apothecary_maxfloors 1
SET   bus_apothecary_district fine shops

self.redis.lpush('bus_apothecary_manager', 'apothecary')

self.redis.lpush('bus_apothecary_managerclass', 'expert')
self.redis.lpush('bus_apothecary_managerclass', 'cleric')
self.redis.lpush('bus_apothecary_managerclass', 'druid')
self.redis.lpush('bus_apothecary_managerclass', 'adept')
self.redis.lpush('bus_apothecary_managerclass', 'sorcerer')
self.redis.lpush('bus_apothecary_managerclass', 'wizard')
self.redis.lpush('bus_apothecary_managerclass', 'ranger')

self.redis.lpush('bus_apothecary_service', 'products')
self.redis.lpush('bus_apothecary_service', 'service')
self.redis.lpush('bus_apothecary_service', 'herbs')
self.redis.lpush('bus_apothecary_service', 'reagents')
self.redis.lpush('bus_apothecary_service', 'spell components')
self.redis.lpush('bus_apothecary_service', 'medicine')

self.redis.lpush('bus_apothecary_trailer', 'shop')
self.redis.lpush('bus_apothecary_trailer', 'shoppe')
self.redis.lpush('bus_apothecary_trailer', 'druggist')

self.redis.lpush('bus_apothecary_smell', 'fresh herbs')
self.redis.lpush('bus_apothecary_smell', 'damp earth')

self.redis.lpush('bus_apothecary_sound', 'a cat mewing')
self.redis.lpush('bus_apothecary_sound', 'a rhythmic scraping')
self.redis.lpush('bus_apothecary_sound', 'silence')
self.redis.lpush('bus_apothecary_sound', 'yelling from the back of the shop')

self.redis.lpush('bus_apothecary_sight', 'bottles/ vials and stacks of grain and herbs')
self.redis.lpush('bus_apothecary_sight', 'a small boy grinding something into powder in a bowl')

########################################################
self.redis.lpush('business_kind', 'bus_armorsmithy')
SET   bus_armorsmithy_kindname armorsmithy
SET   bus_armorsmithy_perbuilding 10

SET   bus_armorsmithy_maxfloors 1
SET   bus_armorsmithy_district trade

self.redis.lpush('bus_armorsmithy_manager', 'armorer')

self.redis.lpush('bus_armorsmithy_managerclass', 'commoner')
self.redis.lpush('bus_armorsmithy_managerclass', 'expert')
self.redis.lpush('bus_armorsmithy_managerclass', 'warrior')
self.redis.lpush('bus_armorsmithy_managerclass', 'fighter')

self.redis.lpush('bus_armorsmithy_service', 'service')

self.redis.lpush('bus_armorsmithy_trailer', 'group')
self.redis.lpush('bus_armorsmithy_trailer', 'armory')

self.redis.lpush('bus_armorsmithy_smell', 'a burning fire')

self.redis.lpush('bus_armorsmithy_sound', 'the sound of a forge')

self.redis.lpush('bus_armorsmithy_sight', 'bit of armor in various states of repair')

########################################################
self.redis.lpush('business_kind', 'bus_astrologer')
SET   bus_astrologer_kindname astrologer
SET   bus_astrologer_perbuilding 1

SET   bus_astrologer_maxfloors 1
SET   bus_astrologer_district fine shops

self.redis.lpush('bus_astrologer_manager', 'astrologer')

self.redis.lpush('bus_astrologer_managerclass', 'expert')
self.redis.lpush('bus_astrologer_managerclass', 'adept')

self.redis.lpush('bus_astrologer_service', 'service')
self.redis.lpush('bus_astrologer_service', 'horoscopes')
self.redis.lpush('bus_astrologer_service', 'birth charts')

self.redis.lpush('bus_astrologer_trailer', 'star gazers')
self.redis.lpush('bus_astrologer_trailer', 'magic eye piece')

self.redis.lpush('bus_astrologer_sight', 'lots of charts with arcane writing on them')
self.redis.lpush('bus_astrologer_sight', 'scrolls leaning against the walls')

########################################################
self.redis.lpush('business_kind', 'bus_bakery')
SET   bus_bakery_kindname bakery
SET   bus_bakery_perbuilding 10

SET   bus_bakery_maxfloors 1
SET   bus_bakery_district shops

self.redis.lpush('bus_bakery_manager', 'baker')
self.redis.lpush('bus_bakery_manager', 'pastrycook')

self.redis.lpush('bus_bakery_managerclass', 'commoner')
self.redis.lpush('bus_bakery_managerclass', 'expert')

self.redis.lpush('bus_bakery_service', 'a warm smile')
self.redis.lpush('bus_bakery_service', 'hot buns')

self.redis.lpush('bus_bakery_trailer', 'bakery')
self.redis.lpush('bus_bakery_trailer', 'sweet house')
self.redis.lpush('bus_bakery_trailer', 'shop')

self.redis.lpush('bus_bakery_smell', 'scent fresh bread')
self.redis.lpush('bus_bakery_smell', 'fresh flour')

self.redis.lpush('bus_bakery_sound', 'yelling in the back of the store')
self.redis.lpush('bus_bakery_sound', 'fire crackling')
self.redis.lpush('bus_bakery_sound', 'a kitten mewing')

self.redis.lpush('bus_bakery_sight', 'fresh rolls')
self.redis.lpush('bus_bakery_sight', 'hot buns')

########################################################
self.redis.lpush('business_kind', 'bus_bank')
SET   bus_bank_kindname bank
SET   bus_bank_perbuilding 30

SET   bus_bank_maxfloors 2
SET   bus_bank_district wealthy

self.redis.lpush('bus_bank_manager', 'banker')

self.redis.lpush('bus_bank_managerclass', 'expert')
self.redis.lpush('bus_bank_managerclass', 'aristocrat')

self.redis.lpush('bus_bank_service', 'service')

self.redis.lpush('bus_bank_trailer', 'money changers')
self.redis.lpush('bus_bank_trailer', 'money lenders')
self.redis.lpush('bus_bank_trailer', 'vault')

self.redis.lpush('bus_bank_smell', 'earth')

self.redis.lpush('bus_bank_sound', 'muffled voices from the back')

self.redis.lpush('bus_bank_sight', 'and empty counter with bars in front of it')

########################################################
self.redis.lpush('business_kind', 'bus_barbershop')
SET   bus_barbershop_kindname barbershop
SET   bus_barbershop_perbuilding 4

SET   bus_barbershop_maxfloors 1
SET   bus_barbershop_district trade

self.redis.lpush('bus_barbershop_manager', 'barber')

self.redis.lpush('bus_barbershop_managerclass', 'commoner')

self.redis.lpush('bus_barbershop_service', 'a good story')
self.redis.lpush('bus_barbershop_service', 'a steady hand')

self.redis.lpush('bus_barbershop_trailer', 'shoppe')
self.redis.lpush('bus_barbershop_trailer', 'shop')

self.redis.lpush('bus_barbershop_smell', 'disinfectant')
self.redis.lpush('bus_barbershop_smell', 'fear')

self.redis.lpush('bus_barbershop_sound', 'snipping scissors')
self.redis.lpush('bus_barbershop_sound', 'a good laugh')
self.redis.lpush('bus_barbershop_sound', 'someone telling a story')

self.redis.lpush('bus_barbershop_sight', 'hair clippings on the floor')
self.redis.lpush('bus_barbershop_sight', 'someone in a chair covered by towels and a sheet')

########################################################
self.redis.lpush('business_kind', 'bus_barrack')
SET   bus_barrack_kindname barrack
SET   bus_barrack_perbuilding 50

SET   bus_barrack_maxfloors 2
SET   bus_barrack_district civic

self.redis.lpush('bus_barrack_manager', 'soldier')

self.redis.lpush('bus_barrack_managerclass', 'expert')
self.redis.lpush('bus_barrack_managerclass', 'warrior')
self.redis.lpush('bus_barrack_managerclass', 'fighter')
self.redis.lpush('bus_barrack_managerclass', 'paladin')

self.redis.lpush('bus_barrack_service', 'service')
self.redis.lpush('bus_barrack_service', 'beds')
self.redis.lpush('bus_barrack_service', 'bunks')

self.redis.lpush('bus_barrack_trailer', 'guard house')
self.redis.lpush('bus_barrack_trailer', 'city guard')
self.redis.lpush('bus_barrack_trailer', 'force')

self.redis.lpush('bus_barrack_smell', 'sweat and beer')

self.redis.lpush('bus_barrack_sound', 'voices')

self.redis.lpush('bus_barrack_sight', 'bunk beds and lockers')

########################################################
self.redis.lpush('business_kind', 'bus_barrister')
SET   bus_barrister_kindname barrister
SET   bus_barrister_perbuilding 10

SET   bus_barrister_maxfloors 3
SET   bus_barrister_district fine shops
self.redis.lpush('bus_barrister_manager', 'lawyer')

self.redis.lpush('bus_barrister_managerclass', 'expert')
self.redis.lpush('bus_barrister_managerclass', 'aristocrat')

self.redis.lpush('bus_barrister_service', 'service')

self.redis.lpush('bus_barrister_trailer', 'house of law')
self.redis.lpush('bus_barrister_trailer', 'and associates')
self.redis.lpush('bus_barrister_trailer', 'legal partners')

self.redis.lpush('bus_barrister_sight', 'a framed contract signed in blood')
self.redis.lpush('bus_barrister_sight', 'massive bookshelves full of legal texts')
self.redis.lpush('bus_barrister_sight', 'cabinets full of case files')

self.redis.lpush('bus_barrister_smell', 'the scent of pork')
self.redis.lpush('bus_barrister_smell', 'the scent of ink and blood')

########################################################
self.redis.lpush('business_kind', 'bus_bathhouse')
SET   bus_bathhouse_kindname bath house
SET   bus_bathhouse_perbuilding 20

SET   bus_bathhouse_maxfloors 1
SET   bus_bathhouse_district trade
self.redis.lpush('bus_bathhouse_manager', 'bather')

self.redis.lpush('bus_bathhouse_managerclass', 'commoner')

self.redis.lpush('bus_bathhouse_service', 'service')
self.redis.lpush('bus_bathhouse_service', 'baths')

self.redis.lpush('bus_bathhouse_trailer', 'bath house')
self.redis.lpush('bus_bathhouse_trailer', 'inspirational waters')

self.redis.lpush('bus_bathhouse_smell', 'soap and flowers')

self.redis.lpush('bus_bathhouse_sound', 'the sound of water running')
self.redis.lpush('bus_bathhouse_sound', 'soft music')
self.redis.lpush('bus_bathhouse_sound', 'low voices')

self.redis.lpush('bus_bathhouse_sight', 'naked people walking around')

########################################################
self.redis.lpush('business_kind', 'bus_beerseller')
SET   bus_beerseller_kindname beer seller
SET   bus_beerseller_perbuilding 4

SET   bus_beerseller_maxfloors 1
SET   bus_beerseller_district market
self.redis.lpush('bus_beerseller_manager', 'beer seller')

self.redis.lpush('bus_beerseller_managerclass', 'commoner')

self.redis.lpush('bus_beerseller_service', 'service')
self.redis.lpush('bus_beerseller_service', 'beer')
self.redis.lpush('bus_beerseller_service', 'brews')

self.redis.lpush('bus_beerseller_trailer', 'tap house')
self.redis.lpush('bus_beerseller_trailer', 'ale house')
self.redis.lpush('bus_beerseller_trailer', 'brewery')

self.redis.lpush('bus_beerseller_smell', 'beer and hops')

self.redis.lpush('bus_beerseller_sight', 'casks of beer')

########################################################
self.redis.lpush('business_kind', 'bus_bleacher')
SET   bus_bleacher_kindname bleacher
SET   bus_bleacher_perbuilding 20

SET   bus_bleacher_maxfloors 1
SET   bus_bleacher_district trade
self.redis.lpush('bus_bleacher_manager', 'bleacher')

self.redis.lpush('bus_bleacher_managerclass', 'commoner')

self.redis.lpush('bus_bleacher_service', 'service')
self.redis.lpush('bus_bleacher_service', 'bleaching')

self.redis.lpush('bus_bleacher_trailer', 'arena')

########################################################
self.redis.lpush('business_kind', 'bus_bookbinder')
SET   bus_bookbinder_kindname bookbinder
SET   bus_bookbinder_perbuilding 20

SET   bus_bookbinder_maxfloors 1
SET   bus_bookbinder_district industry

self.redis.lpush('bus_bookbinder_manager', 'bookbinder')

self.redis.lpush('bus_bookbinder_managerclass', 'commoner')
self.redis.lpush('bus_bookbinder_managerclass', 'expert')

self.redis.lpush('bus_bookbinder_service', 'service')

self.redis.lpush('bus_bookbinder_trailer', 'bindery')
self.redis.lpush('bus_bookbinder_trailer', 'shoppe')
self.redis.lpush('bus_bookbinder_trailer', 'book smith')

self.redis.lpush('bus_bookbinder_smell', 'old parchment')

self.redis.lpush('bus_bookbinder_sight', 'books and papers everywhere')

########################################################
self.redis.lpush('business_kind', 'bus_bookstore')
SET   bus_bookstore_kindname bookstore
SET   bus_bookstore_perbuilding 4

SET   bus_bookstore_maxfloors 3
SET   bus_bookstore_district fine shops
self.redis.lpush('bus_bookstore_manager', 'bookseller')

self.redis.lpush('bus_bookstore_managerclass', 'commoner')
self.redis.lpush('bus_bookstore_managerclass', 'expert')

self.redis.lpush('bus_bookstore_service', 'service')
self.redis.lpush('bus_bookstore_service', 'books')
self.redis.lpush('bus_bookstore_service', 'tomes')

self.redis.lpush('bus_bookstore_trailer', 'fine books')
self.redis.lpush('bus_bookstore_trailer', 'book smith')

########################################################
self.redis.lpush('business_kind', 'bus_bowyer')
SET   bus_bowyer_kindname bowyer
SET   bus_bowyer_perbuilding 5

SET   bus_bowyer_maxfloors 1
SET   bus_bowyer_district trade
self.redis.lpush('bus_bowyer_manager', 'bowyer')

self.redis.lpush('bus_bowyer_managerclass', 'expert')
self.redis.lpush('bus_bowyer_managerclass', 'ranger')

self.redis.lpush('bus_bowyer_service', 'service')
self.redis.lpush('bus_bowyer_service', 'bows')
self.redis.lpush('bus_bowyer_service', 'bow repairs')
self.redis.lpush('bus_bowyer_service', 'replacement bows')

self.redis.lpush('bus_bowyer_trailer', 'fine bows')
self.redis.lpush('bus_bowyer_trailer', 'archery')

########################################################
self.redis.lpush('business_kind', 'bus_brewery')
SET   bus_brewery_kindname brewery
SET   bus_brewery_perbuilding 20

SET   bus_brewery_maxfloors 3
SET   bus_brewery_district industry
self.redis.lpush('bus_brewery_manager', 'brewer')

self.redis.lpush('bus_brewery_managerclass', 'commoner')
self.redis.lpush('bus_brewery_managerclass', 'expert')

self.redis.lpush('bus_brewery_service', 'service')
self.redis.lpush('bus_brewery_service', 'beer')
self.redis.lpush('bus_brewery_service', 'ale')
self.redis.lpush('bus_brewery_service', 'grog')
self.redis.lpush('bus_brewery_service', 'lager')

self.redis.lpush('bus_brewery_trailer', 'brewery')
self.redis.lpush('bus_brewery_trailer', 'beer garden')
self.redis.lpush('bus_brewery_trailer', 'pub')

self.redis.lpush('bus_brewery_smell', 'hops and grain')

self.redis.lpush('bus_brewery_sound', 'people singing')
self.redis.lpush('bus_brewery_sound', 'laughing')

self.redis.lpush('bus_brewery_sight', 'piles of grain')
self.redis.lpush('bus_brewery_sight', 'bags of hops')

########################################################
self.redis.lpush('business_kind', 'bus_brothel')
SET   bus_brothel_kindname brothel
SET   bus_brothel_perbuilding 20

SET   bus_brothel_maxfloors 2
SET   bus_brothel_district poor
self.redis.lpush('bus_brothel_manager', 'prostitute')

self.redis.lpush('bus_brothel_managerclass', 'commoner')

self.redis.lpush('bus_brothel_service', 'service')
self.redis.lpush('bus_brothel_service', 'long back rubs')

self.redis.lpush('bus_brothel_trailer', 'house of ill repute')
self.redis.lpush('bus_brothel_trailer', 'whorehouse')
self.redis.lpush('bus_brothel_trailer', 'temple')

self.redis.lpush('bus_brothel_smell', 'scent of oil')
self.redis.lpush('bus_brothel_smell', 'perfume')

self.redis.lpush('bus_brothel_sound', 'loud moaning')
self.redis.lpush('bus_brothel_sound', 'quiet music')
self.redis.lpush('bus_brothel_sound', 'girls giggling')

self.redis.lpush('bus_brothel_sight', 'barely clothed women')
self.redis.lpush('bus_brothel_sight', 'candles and drapery')

########################################################
self.redis.lpush('business_kind', 'bus_bucklery')
SET   bus_bucklery_kindname bucklery
SET   bus_bucklery_perbuilding 5

SET   bus_bucklery_maxfloors 1
SET   bus_bucklery_district shop
self.redis.lpush('bus_bucklery_manager', 'bucklemaker')

self.redis.lpush('bus_bucklery_managerclass', 'commoner')
self.redis.lpush('bus_bucklery_managerclass', 'expert')

self.redis.lpush('bus_bucklery_service', 'service')
self.redis.lpush('bus_bucklery_service', 'buckles')

self.redis.lpush('bus_bucklery_trailer', 'buckler')

########################################################
self.redis.lpush('business_kind', 'bus_butchershop')
SET   bus_butchershop_kindname butchershop
SET   bus_butchershop_perbuilding 10

SET   bus_butchershop_maxfloors 1
SET   bus_butchershop_district market
self.redis.lpush('bus_butchershop_manager', 'butcher')

self.redis.lpush('bus_butchershop_managerclass', 'commoner')
self.redis.lpush('bus_butchershop_managerclass', 'expert')

self.redis.lpush('bus_butchershop_service', 'service')
self.redis.lpush('bus_butchershop_service', 'lamb')
self.redis.lpush('bus_butchershop_service', 'ham')
self.redis.lpush('bus_butchershop_service', 'steaks')
self.redis.lpush('bus_butchershop_service', 'shanks')
self.redis.lpush('bus_butchershop_service', 'ribs')
self.redis.lpush('bus_butchershop_service', 'venison')

self.redis.lpush('bus_butchershop_trailer', 'meat handlers')
self.redis.lpush('bus_butchershop_trailer', 'meat house')
self.redis.lpush('bus_butchershop_trailer', 'butchers')

########################################################
self.redis.lpush('business_kind', 'bus_cartwright')
SET   bus_cartwright_kindname cartwright
SET   bus_cartwright_perbuilding 10

SET   bus_cartwright_maxfloors 1
SET   bus_cartwright_district industry
self.redis.lpush('bus_cartwright_manager', 'cartwright')

self.redis.lpush('bus_cartwright_managerclass', 'commoner')
self.redis.lpush('bus_cartwright_managerclass', 'expert')

self.redis.lpush('bus_cartwright_service', 'service')
self.redis.lpush('bus_cartwright_service', 'spoke replacements')
self.redis.lpush('bus_cartwright_service', 'axle replacements')
self.redis.lpush('bus_cartwright_service', 'carts')
self.redis.lpush('bus_cartwright_service', 'wheel repairs')
self.redis.lpush('bus_cartwright_service', 'wheel replacements')
self.redis.lpush('bus_cartwright_service', 'wheels')

self.redis.lpush('bus_cartwright_trailer', 'shop')
self.redis.lpush('bus_cartwright_trailer', 'wainwright')
self.redis.lpush('bus_cartwright_trailer', 'cart repairs')

########################################################
self.redis.lpush('business_kind', 'bus_chandleryshop')
SET   bus_chandleryshop_kindname chandlery shop
SET   bus_chandleryshop_perbuilding 10

SET   bus_chandleryshop_maxfloors 1
SET   bus_chandleryshop_district industry
self.redis.lpush('bus_chandleryshop_manager', 'chandler')

self.redis.lpush('bus_chandleryshop_managerclass', 'commoner')
self.redis.lpush('bus_chandleryshop_managerclass', 'expert')

self.redis.lpush('bus_chandleryshop_service', 'service')
self.redis.lpush('bus_chandleryshop_service', 'candles')

self.redis.lpush('bus_chandleryshop_trailer', 'supplies')

########################################################
self.redis.lpush('business_kind', 'bus_cheeseshop')
SET   bus_cheeseshop_kindname cheeseshop
SET   bus_cheeseshop_perbuilding 20

SET   bus_cheeseshop_maxfloors 1
SET   bus_cheeseshop_district trade
self.redis.lpush('bus_cheeseshop_manager', 'cheesemaker')

self.redis.lpush('bus_cheeseshop_managerclass', 'commoner')
self.redis.lpush('bus_cheeseshop_managerclass', 'expert')

self.redis.lpush('bus_cheeseshop_service', 'service')
self.redis.lpush('bus_cheeseshop_service', 'cheese')
self.redis.lpush('bus_cheeseshop_service', 'brie')
self.redis.lpush('bus_cheeseshop_service', 'bleu')
self.redis.lpush('bus_cheeseshop_service', 'cheddar')
self.redis.lpush('bus_cheeseshop_service', 'cheese wheels')

self.redis.lpush('bus_cheeseshop_trailer', 'shoppe')

self.redis.lpush('bus_cheeseshop_smell', 'a slightly sweet smell of cheese')

self.redis.lpush('bus_cheeseshop_sound', 'yelling in the back')

self.redis.lpush('bus_cheeseshop_sight', 'many wheels of cheese')
self.redis.lpush('bus_cheeseshop_sight', 'jugs of milk and other tools')

########################################################
self.redis.lpush('business_kind', 'bus_church')
SET   bus_church_kindname church
SET   bus_church_perbuilding 10

SET   bus_church_maxfloors 1
SET   bus_church_district mercy
self.redis.lpush('bus_church_manager', 'priest')

self.redis.lpush('bus_church_managerclass', 'commoner')
self.redis.lpush('bus_church_managerclass', 'expert')
self.redis.lpush('bus_church_managerclass', 'monk')
self.redis.lpush('bus_church_managerclass', 'cleric')
self.redis.lpush('bus_church_managerclass', 'druid')
self.redis.lpush('bus_church_managerclass', 'paladin')

self.redis.lpush('bus_church_service', 'long prayers')
self.redis.lpush('bus_church_service', 'clean sacrifices')

self.redis.lpush('bus_church_trailer', 'temple')
self.redis.lpush('bus_church_trailer', 'shrine')
self.redis.lpush('bus_church_trailer', 'of all that is holy')

self.redis.lpush('bus_church_smell', 'scent of oil')
self.redis.lpush('bus_church_smellsmell', 'of blood')
self.redis.lpush('bus_church_smell', 'weapons being sharpened')

self.redis.lpush('bus_church_sound', 'rhythmic chanting')
self.redis.lpush('bus_church_sound', 'a low moaning')
self.redis.lpush('bus_church_sound', 'silence')

self.redis.lpush('bus_church_sight', 'people walking around in a daze')
self.redis.lpush('bus_church_sight', 'elegant golden decorations all around')

########################################################
self.redis.lpush('business_kind', 'bus_civiccenter')
SET   bus_civiccenter_kindname civic center
SET   bus_civiccenter_perbuilding 30

SET   bus_civiccenter_maxfloors 3
SET   bus_civiccenter_district civic
self.redis.lpush('bus_civiccenter_manager', 'official')

self.redis.lpush('bus_civiccenter_managerclass', 'commoner')
self.redis.lpush('bus_civiccenter_managerclass', 'expert')
self.redis.lpush('bus_civiccenter_managerclass', 'aristocrat')

self.redis.lpush('bus_civiccenter_service', 'service')

self.redis.lpush('bus_civiccenter_trailer', 'house')
self.redis.lpush('bus_civiccenter_trailer', 'arena')

########################################################
self.redis.lpush('business_kind', 'bus_clinic')
SET   bus_clinic_kindname clinic
SET   bus_clinic_perbuilding 10

SET   bus_clinic_maxfloors 2
SET   bus_clinic_district mercy
self.redis.lpush('bus_clinic_manager', 'physician')

self.redis.lpush('bus_clinic_managerclass', 'commoner')
self.redis.lpush('bus_clinic_managerclass', 'expert')
self.redis.lpush('bus_clinic_managerclass', 'cleric')
self.redis.lpush('bus_clinic_managerclass', 'adept')

self.redis.lpush('bus_clinic_service', 'service')

self.redis.lpush('bus_clinic_trailer', 'clinic')
self.redis.lpush('bus_clinic_trailer', 'healers')

########################################################
self.redis.lpush('business_kind', 'bus_clothingshop')
SET   bus_clothingshop_kindname clothing shop
SET   bus_clothingshop_perbuilding 20

SET   bus_clothingshop_maxfloors 2
SET   bus_clothingshop_district shops
self.redis.lpush('bus_clothingshop_manager', 'tailor')

self.redis.lpush('bus_clothingshop_managerclass', 'commoner')
self.redis.lpush('bus_clothingshop_managerclass', 'expert')

self.redis.lpush('bus_clothingshop_service', 'service')
self.redis.lpush('bus_clothingshop_service', 'tunics')
self.redis.lpush('bus_clothingshop_service', 'skirts')
self.redis.lpush('bus_clothingshop_service', 'pants')
self.redis.lpush('bus_clothingshop_service', 'underwear')
self.redis.lpush('bus_clothingshop_service', 'stockings')
self.redis.lpush('bus_clothingshop_service', 'coats')
self.redis.lpush('bus_clothingshop_service', 'shirts')

self.redis.lpush('bus_clothingshop_trailer', 'wares')
self.redis.lpush('bus_clothingshop_trailer', 'shop')

########################################################
self.redis.lpush('business_kind', 'bus_cobbler')
SET   bus_cobbler_kindname cobblershop
SET   bus_cobbler_perbuilding 4

SET   bus_cobbler_maxfloors 2
SET   bus_cobbler_district market
self.redis.lpush('bus_cobbler_manager', 'cobbler')

self.redis.lpush('bus_cobbler_managerclass', 'commoner')
self.redis.lpush('bus_cobbler_managerclass', 'expert')

self.redis.lpush('bus_cobbler_service', 'work')
self.redis.lpush('bus_cobbler_service', 'goods')
self.redis.lpush('bus_cobbler_service', 'new soles')
self.redis.lpush('bus_cobbler_service', 'softer insoles')
self.redis.lpush('bus_cobbler_service', 'repairs')

self.redis.lpush('bus_cobbler_trailer', 'shoppe')
self.redis.lpush('bus_cobbler_trailer', 'shop')

self.redis.lpush('bus_cobbler_smell', 'scent of leather')
self.redis.lpush('bus_cobbler_smell', 'rhythmic grinding')

self.redis.lpush('bus_cobbler_sound', 'silence')
self.redis.lpush('bus_cobbler_sound', 'the work of shoes')
self.redis.lpush('bus_cobbler_sound', 'a kitten mewing')

self.redis.lpush('bus_cobbler_sight', 'old shoes and bit of leather')
self.redis.lpush('bus_cobbler_sight', 'a kitten')

########################################################
self.redis.lpush('business_kind', 'bus_cooperage')
SET   bus_cooperage_kindname cooperage
SET   bus_cooperage_perbuilding 10

SET   bus_cooperage_maxfloors 1
SET   bus_cooperage_district industry
self.redis.lpush('bus_cooperage_manager', 'cooper')

self.redis.lpush('bus_cooperage_managerclass', 'commoner')
self.redis.lpush('bus_cooperage_managerclass', 'expert')

self.redis.lpush('bus_cooperage_service', 'service')
self.redis.lpush('bus_cooperage_service', 'barrels')
self.redis.lpush('bus_cooperage_service', 'buckets')
self.redis.lpush('bus_cooperage_service', 'casks')
self.redis.lpush('bus_cooperage_service', 'butter churns')

self.redis.lpush('bus_cooperage_trailer', 'barrels')
self.redis.lpush('bus_cooperage_trailer', 'coop hoop')

########################################################
self.redis.lpush('business_kind', 'bus_copyoffice')
SET   bus_copyoffice_kindname copyoffice
SET   bus_copyoffice_perbuilding 20

SET   bus_copyoffice_maxfloors 3
SET   bus_copyoffice_district professional
self.redis.lpush('bus_copyoffice_manager', 'copyist')

self.redis.lpush('bus_copyoffice_managerclass', 'commoner')
self.redis.lpush('bus_copyoffice_managerclass', 'expert')

self.redis.lpush('bus_copyoffice_service', 'service')
self.redis.lpush('bus_copyoffice_service', 'copies')

self.redis.lpush('bus_copyoffice_trailer', 'scribe')
self.redis.lpush('bus_copyoffice_trailer', 'shop')

########################################################
self.redis.lpush('business_kind', 'bus_cutlery')
SET   bus_cutlery_kindname cutlery shop
SET   bus_cutlery_perbuilding 5

SET   bus_cutlery_maxfloors 1
SET   bus_cutlery_district trade
self.redis.lpush('bus_cutlery_manager', 'cutler')

self.redis.lpush('bus_cutlery_managerclass', 'commoner')
self.redis.lpush('bus_cutlery_managerclass', 'expert')

self.redis.lpush('bus_cutlery_service', 'service')
self.redis.lpush('bus_cutlery_service', 'spoons')
self.redis.lpush('bus_cutlery_service', 'knives')
self.redis.lpush('bus_cutlery_service', 'forks')

self.redis.lpush('bus_cutlery_trailer', 'chop house')
self.redis.lpush('bus_cutlery_trailer', 'fine forks')

########################################################
self.redis.lpush('business_kind', 'bus_dyer')
SET   bus_dyer_kindname dyer
SET   bus_dyer_perbuilding 20

SET   bus_dyer_maxfloors 1
SET   bus_dyer_district trade
self.redis.lpush('bus_dyer_manager', 'dyer')

self.redis.lpush('bus_dyer_managerclass', 'commoner')
self.redis.lpush('bus_dyer_managerclass', 'expert')

self.redis.lpush('bus_dyer_service', 'service')

self.redis.lpush('bus_dyer_trailer', 'color shop')
self.redis.lpush('bus_dyer_trailer', 'house of colors')

self.redis.lpush('bus_dyer_smell', 'something fishy')

self.redis.lpush('bus_dyer_sound', 'a bubbling sound')

self.redis.lpush('bus_dyer_sight', 'lots of colored cloth and pots of dye')

########################################################
self.redis.lpush('business_kind', 'bus_engineering')
SET   bus_engineering_kindname engineering firm
SET   bus_engineering_perbuilding 20

SET   bus_engineering_maxfloors 3
SET   bus_engineering_district professional
self.redis.lpush('bus_engineering_manager', 'engineer')

self.redis.lpush('bus_engineering_managerclass', 'commoner')
self.redis.lpush('bus_engineering_managerclass', 'expert')

self.redis.lpush('bus_engineering_service', 'service')

self.redis.lpush('bus_engineering_trailer', 'designs')
self.redis.lpush('bus_engineering_trailer', 'builders')

########################################################
self.redis.lpush('business_kind', 'bus_fishery')
SET   bus_fishery_kindname fishery
SET   bus_fishery_perbuilding 20

SET   bus_fishery_maxfloors 1
SET   bus_fishery_district industry
self.redis.lpush('bus_fishery_manager', 'fishmonger')

self.redis.lpush('bus_fishery_managerclass', 'commoner')
self.redis.lpush('bus_fishery_managerclass', 'expert')

self.redis.lpush('bus_fishery_service', 'service')
self.redis.lpush('bus_fishery_service', 'fish')

self.redis.lpush('bus_fishery_trailer', 'fish camp')
self.redis.lpush('bus_fishery_trailer', 'fish house')
self.redis.lpush('bus_fishery_trailer', 'sport house')

self.redis.lpush('bus_fishery_smell', 'something fishy')
self.redis.lpush('bus_fishery_smell', 'no fish')

########################################################
self.redis.lpush('business_kind', 'bus_furtrade')
SET   bus_furtrade_kindname furtrade
SET   bus_furtrade_perbuilding 20

SET   bus_furtrade_maxfloors 1
SET   bus_furtrade_district trade
self.redis.lpush('bus_furtrade_manager', 'furrier')

self.redis.lpush('bus_furtrade_managerclass', 'commoner')
self.redis.lpush('bus_furtrade_managerclass', 'expert')
self.redis.lpush('bus_furtrade_managerclass', 'ranger')

self.redis.lpush('bus_furtrade_service', 'service')
self.redis.lpush('bus_furtrade_service', 'pelts')
self.redis.lpush('bus_furtrade_service', 'furs')

self.redis.lpush('bus_furtrade_trailer', 'furs')

########################################################
self.redis.lpush('business_kind', 'bus_generalstore')
SET   bus_generalstore_kindname general store
SET   bus_generalstore_perbuilding 4

SET   bus_generalstore_maxfloors 2
SET   bus_generalstore_district market
self.redis.lpush('bus_generalstore_manager', 'outfitter')

self.redis.lpush('bus_generalstore_managerclass', 'commoner')
self.redis.lpush('bus_generalstore_managerclass', 'expert')

self.redis.lpush('bus_generalstore_service', 'service')
self.redis.lpush('bus_generalstore_service', 'goods')

self.redis.lpush('bus_generalstore_trailer', 'general store')
self.redis.lpush('bus_generalstore_trailer', 'general merchandise')
self.redis.lpush('bus_generalstore_trailer', 'dry goods')

########################################################
self.redis.lpush('business_kind', 'bus_glassmaker')
SET   bus_glassmaker_kindname glassmaker hut
SET   bus_glassmaker_perbuilding 10

SET   bus_glassmaker_maxfloors 1
SET   bus_glassmaker_district trade
self.redis.lpush('bus_glassmaker_manager', 'glassmaker')

self.redis.lpush('bus_glassmaker_managerclass', 'commoner')
self.redis.lpush('bus_glassmaker_managerclass', 'expert')

self.redis.lpush('bus_glassmaker_service', 'service')
self.redis.lpush('bus_glassmaker_service', 'glass')
self.redis.lpush('bus_glassmaker_service', 'ornaments')

self.redis.lpush('bus_glassmaker_trailer', 'blowers')
self.redis.lpush('bus_glassmaker_trailer', 'glass crafters')

self.redis.lpush('bus_glassmaker_smell', 'a burning forge')

self.redis.lpush('bus_glassmaker_sound', 'a bellows pumping')

self.redis.lpush('bus_glassmaker_sight', 'panes of glass and mirrors')

########################################################
self.redis.lpush('business_kind', 'bus_gloveshop')
SET   bus_gloveshop_kindname glove shop
SET   bus_gloveshop_perbuilding 5

SET   bus_gloveshop_maxfloors 1
SET   bus_gloveshop_district trade
self.redis.lpush('bus_gloveshop_manager', 'glovemaker')

self.redis.lpush('bus_gloveshop_managerclass', 'commoner')
self.redis.lpush('bus_gloveshop_managerclass', 'expert')

self.redis.lpush('bus_gloveshop_service', 'service')
self.redis.lpush('bus_gloveshop_service', 'gloves')

self.redis.lpush('bus_gloveshop_trailer', 'gloves')
self.redis.lpush('bus_gloveshop_trailer', 'glove makers')
self.redis.lpush('bus_gloveshop_trailer', 'glove shop')
self.redis.lpush('bus_gloveshop_trailer', 'shoppe')

########################################################
self.redis.lpush('business_kind', 'bus_graveyard')
SET   bus_graveyard_kindname graveyard
SET   bus_graveyard_perbuilding 10

SET   bus_graveyard_maxfloors 1
SET   bus_graveyard_district mercy
self.redis.lpush('bus_graveyard_manager', 'undertaker')

self.redis.lpush('bus_graveyard_managerclass', 'commoner')
self.redis.lpush('bus_graveyard_managerclass', 'expert')
self.redis.lpush('bus_graveyard_managerclass', 'cleric')

self.redis.lpush('bus_graveyard_service', 'service')
self.redis.lpush('bus_graveyard_service', 'plots')
self.redis.lpush('bus_graveyard_service', 'grave sites')

self.redis.lpush('bus_graveyard_trailer', 'grave diggers')
self.redis.lpush('bus_graveyard_trailer', 'night smiths')

########################################################
self.redis.lpush('business_kind', 'bus_grocerystore')
SET   bus_grocerystore_kindname grocery store
SET   bus_grocerystore_perbuilding 10

SET   bus_grocerystore_maxfloors 1
SET   bus_grocerystore_district market
self.redis.lpush('bus_grocerystore_manager', 'grocer')

self.redis.lpush('bus_grocerystore_managerclass', 'commoner')
self.redis.lpush('bus_grocerystore_managerclass', 'expert')

self.redis.lpush('bus_grocerystore_service', 'service')
self.redis.lpush('bus_grocerystore_service', 'food')
self.redis.lpush('bus_grocerystore_service', 'produce')

self.redis.lpush('bus_grocerystore_trailer', 'dry goods')
self.redis.lpush('bus_grocerystore_trailer', 'general merchandise')

########################################################
self.redis.lpush('business_kind', 'bus_harnessmaker')
SET   bus_harnessmaker_kindname harness maker
SET   bus_harnessmaker_perbuilding 5

SET   bus_harnessmaker_maxfloors 1
SET   bus_harnessmaker_district shops

self.redis.lpush('bus_harnessmaker_manager', 'harness maker')

self.redis.lpush('bus_harnessmaker_managerclass', 'commoner')
self.redis.lpush('bus_harnessmaker_managerclass', 'expert')

self.redis.lpush('bus_harnessmaker_service', 'service')
self.redis.lpush('bus_harnessmaker_service', 'harnesses')

self.redis.lpush('bus_harnessmaker_trailer', 'leather goods')
self.redis.lpush('bus_harnessmaker_trailer', 'harnesses')

########################################################
self.redis.lpush('business_kind', 'bus_hatshop')
SET   bus_hatshop_kindname hat shop
SET   bus_hatshop_perbuilding 10

SET   bus_hatshop_maxfloors 1
SET   bus_hatshop_district shops

self.redis.lpush('bus_hatshop_manager', 'hatmaker')

self.redis.lpush('bus_hatshop_managerclass', 'commoner')
self.redis.lpush('bus_hatshop_managerclass', 'expert')

self.redis.lpush('bus_hatshop_service', 'service')
self.redis.lpush('bus_hatshop_service', 'hats')
self.redis.lpush('bus_hatshop_service', 'caps')

self.redis.lpush('bus_hatshop_trailer', 'hats shop')
self.redis.lpush('bus_hatshop_trailer', 'hatters')

########################################################
self.redis.lpush('business_kind', 'bus_haymerchant')
SET   bus_haymerchant_kindname haymerchant
SET   bus_haymerchant_perbuilding 5

SET   bus_haymerchant_maxfloors 2
SET   bus_haymerchant_district industry

self.redis.lpush('bus_haymerchant_manager', 'haymerchant')

self.redis.lpush('bus_haymerchant_managerclass', 'commoner')
self.redis.lpush('bus_haymerchant_managerclass', 'expert')

self.redis.lpush('bus_haymerchant_service', 'service')
self.redis.lpush('bus_haymerchant_service', 'hay')

self.redis.lpush('bus_haymerchant_trailer', 'farms')
self.redis.lpush('bus_haymerchant_trailer', 'farmers market')

########################################################
self.redis.lpush('business_kind', 'bus_herbalist')
SET   bus_herbalist_kindname herbalist shop
SET   bus_herbalist_perbuilding 5

SET   bus_herbalist_maxfloors 1
SET   bus_herbalist_district fine shops

self.redis.lpush('bus_herbalist_manager', 'herbalist')

self.redis.lpush('bus_herbalist_managerclass', 'commoner')
self.redis.lpush('bus_herbalist_managerclass', 'expert')
self.redis.lpush('bus_herbalist_managerclass', 'cleric')
self.redis.lpush('bus_herbalist_managerclass', 'druid')
self.redis.lpush('bus_herbalist_managerclass', 'adept')
self.redis.lpush('bus_herbalist_managerclass', 'sorcerer')
self.redis.lpush('bus_herbalist_managerclass', 'wizard')
self.redis.lpush('bus_herbalist_managerclass', 'ranger')

self.redis.lpush('bus_herbalist_service', 'service')
self.redis.lpush('bus_herbalist_service', 'herbs')

self.redis.lpush('bus_herbalist_trailer', 'herbalist')

########################################################
self.redis.lpush('business_kind', 'bus_illuminator')
SET   bus_illuminator_kindname illuminator
SET   bus_illuminator_perbuilding 5

SET   bus_illuminator_maxfloors 1
SET   bus_illuminator_district fine shops

self.redis.lpush('bus_illuminator_manager', 'illuminator')

self.redis.lpush('bus_illuminator_managerclass', 'commoner')
self.redis.lpush('bus_illuminator_managerclass', 'expert')

self.redis.lpush('bus_illuminator_service', 'service')
self.redis.lpush('bus_illuminator_service', 'illustrations')
self.redis.lpush('bus_illuminator_service', 'artwork')

self.redis.lpush('bus_illuminator_trailer', 'candle maker')

########################################################
self.redis.lpush('business_kind', 'bus_inn')
SET   bus_inn_kindname inn
SET   bus_inn_perbuilding 3

SET   bus_inn_maxfloors 5
SET   bus_inn_district shops

self.redis.lpush('bus_inn_manager', 'innkeeper')

self.redis.lpush('bus_inn_managerclass', 'commoner')

self.redis.lpush('bus_inn_service', 'service')
self.redis.lpush('bus_inn_service', 'rooms')

self.redis.lpush('bus_inn_trailer', 'hostel')
self.redis.lpush('bus_inn_trailer', 'inn')
self.redis.lpush('bus_inn_trailer', 'lodge')

########################################################
self.redis.lpush('business_kind', 'bus_jailhouse')
SET   bus_jailhouse_kindname jailhouse
SET   bus_jailhouse_perbuilding 10

SET   bus_jailhouse_maxfloors 3
SET   bus_jailhouse_district prison

self.redis.lpush('bus_jailhouse_manager', 'jailer')

self.redis.lpush('bus_jailhouse_managerclass', 'commoner')
self.redis.lpush('bus_jailhouse_managerclass', 'warrior')

self.redis.lpush('bus_jailhouse_service', 'service')

self.redis.lpush('bus_jailhouse_trailer', 'public jail')
self.redis.lpush('bus_jailhouse_trailer', 'prison')
self.redis.lpush('bus_jailhouse_trailer', 'correctional center')
self.redis.lpush('bus_jailhouse_trailer', 'work camp')
self.redis.lpush('bus_jailhouse_trailer', 'gaol')

########################################################
self.redis.lpush('business_kind', 'bus_jeweler')
SET   bus_jeweler_kindname jewelry store
SET   bus_jeweler_perbuilding 10

SET   bus_jeweler_maxfloors 2
SET   bus_jeweler_district shops

self.redis.lpush('bus_jeweler_manager', 'jeweler')

self.redis.lpush('bus_jeweler_managerclass', 'commoner')
self.redis.lpush('bus_jeweler_managerclass', 'expert')
self.redis.lpush('bus_jeweler_managerclass', 'rogue')
self.redis.lpush('bus_jeweler_managerclass', 'aristocrat')

self.redis.lpush('bus_jeweler_service', 'service')
self.redis.lpush('bus_jeweler_service', 'cuts')
self.redis.lpush('bus_jeweler_service', 'gems')
self.redis.lpush('bus_jeweler_service', 'rings')
self.redis.lpush('bus_jeweler_service', 'pendants')
self.redis.lpush('bus_jeweler_service', 'necklaces')
self.redis.lpush('bus_jeweler_service', 'bracelets')

self.redis.lpush('bus_jeweler_trailer', 'jewelers')

########################################################
self.redis.lpush('business_kind', 'bus_shrine')
SET   bus_shrine_kindname shrine
SET   bus_shrine_perbuilding 10

SET   bus_shrine_maxfloors 2
SET   bus_shrine_district mercy

self.redis.lpush('bus_shrine_manager', 'priest')

self.redis.lpush('bus_shrine_managerclass', 'commoner')
self.redis.lpush('bus_shrine_managerclass', 'expert')
self.redis.lpush('bus_shrine_managerclass', 'monk')
self.redis.lpush('bus_shrine_managerclass', 'cleric')
self.redis.lpush('bus_shrine_managerclass', 'druid')
self.redis.lpush('bus_shrine_managerclass', 'paladin')

self.redis.lpush('bus_shrine_service', 'service')

self.redis.lpush('bus_shrine_trailer', 'shrine')
self.redis.lpush('bus_shrine_trailer', 'temple')
self.redis.lpush('bus_shrine_trailer', 'worship house')

########################################################
self.redis.lpush('business_kind', 'bus_temple')
SET   bus_temple_kindname temple
SET   bus_temple_perbuilding 10

SET   bus_temple_maxfloors 1
SET   bus_temple_district mercy

self.redis.lpush('bus_temple_manager', 'priest')

self.redis.lpush('bus_temple_managerclass', 'commoner')
self.redis.lpush('bus_temple_managerclass', 'monk')
self.redis.lpush('bus_temple_managerclass', 'cleric')
self.redis.lpush('bus_temple_managerclass', 'druid')
self.redis.lpush('bus_temple_managerclass', 'paladin')

self.redis.lpush('bus_temple_service', 'service')

self.redis.lpush('bus_temple_trailer', 'shrine')
self.redis.lpush('bus_temple_trailer', 'temple')
self.redis.lpush('bus_temple_trailer', 'worship house')

########################################################
self.redis.lpush('business_kind', 'bus_almhouse')
SET   bus_almhouse_kindname almshouse
SET   bus_almhouse_perbuilding 10

SET   bus_almhouse_maxfloors 4
SET   bus_almhouse_district civic

self.redis.lpush('bus_almhouse_manager', 'social worker')

self.redis.lpush('bus_almhouse_managerclass', 'cleric')
self.redis.lpush('bus_almhouse_managerclass', 'commoner')

self.redis.lpush('bus_almhouse_service', 'service')

self.redis.lpush('bus_almhouse_trailer', 'charity')
self.redis.lpush('bus_almhouse_trailer', 'poor house')

########################################################
self.redis.lpush('business_kind', 'bus_boathouse')
SET   bus_boathouse_kindname boat for hire
SET   bus_boathouse_perbuilding 1

SET   bus_boathouse_maxfloors 1
SET   bus_boathouse_district port

self.redis.lpush('bus_boathouse_manager', 'ship captain')

self.redis.lpush('bus_boathouse_managerclass', 'commoner')
self.redis.lpush('bus_boathouse_managerclass', 'expert')

self.redis.lpush('bus_boathouse_service', 'service')

self.redis.lpush('bus_boathouse_trailer', 'docs')
self.redis.lpush('bus_boathouse_trailer', 'wharf')

########################################################
self.redis.lpush('business_kind', 'bus_firepit')
SET   bus_firepit_kindname firepit
SET   bus_firepit_perbuilding 10

SET   bus_firepit_maxfloors 1
SET   bus_firepit_district industry

self.redis.lpush('bus_firepit_manager', 'collier')

self.redis.lpush('bus_firepit_managerclass', 'commoner')

self.redis.lpush('bus_firepit_service', 'service')

self.redis.lpush('bus_firepit_trailer', 'charcoalers')
self.redis.lpush('bus_firepit_trailer', 'firepit')
self.redis.lpush('bus_firepit_trailer', 'shoppe')

########################################################
self.redis.lpush('business_kind', 'bus_hospital')
SET   bus_hospital_kindname hospital
SET   bus_hospital_perbuilding 10

SET   bus_hospital_maxfloors 3
SET   bus_hospital_district industry

self.redis.lpush('bus_hospital_manager', 'doctor')

self.redis.lpush('bus_hospital_managerclass', 'cleric')
self.redis.lpush('bus_hospital_managerclass', 'commoner')
self.redis.lpush('bus_hospital_managerclass', 'expert')

self.redis.lpush('bus_hospital_service', 'service')

self.redis.lpush('bus_hospital_trailer', 'healers')
self.redis.lpush('bus_hospital_trailer', 'clinic')
self.redis.lpush('bus_hospital_trailer', 'healing house')

########################################################
self.redis.lpush('business_kind', 'bus_hostel')
SET   bus_hostel_kindname hostel
SET   bus_hostel_perbuilding 10

SET   bus_hostel_maxfloors 4
SET   bus_hostel_district mercy

self.redis.lpush('bus_hostel_manager', 'good Samaritan')

self.redis.lpush('bus_hostel_managerclass', 'adept')
self.redis.lpush('bus_hostel_managerclass', 'cleric')
self.redis.lpush('bus_hostel_managerclass', 'commoner')

self.redis.lpush('bus_hostel_service', 'service')
self.redis.lpush('bus_hostel_service', 'rooms')
self.redis.lpush('bus_hostel_service', 'beds')

self.redis.lpush('bus_hostel_trailer', 'Hostel')
self.redis.lpush('bus_hostel_trailer', 'Youth Hostel')

########################################################
self.redis.lpush('business_kind', 'bus_junkyard')
SET   bus_junkyard_kindname junkyard
SET   bus_junkyard_perbuilding 10

SET   bus_junkyard_maxfloors 1
SET   bus_junkyard_district trade

self.redis.lpush('bus_junkyard_manager', 'tinker')

self.redis.lpush('bus_junkyard_managerclass', 'commoner')
self.redis.lpush('bus_junkyard_managerclass', 'expert')

self.redis.lpush('bus_junkyard_service', 'service')
self.redis.lpush('bus_junkyard_service', 'parts')
self.redis.lpush('bus_junkyard_service', 'junk')

self.redis.lpush('bus_junkyard_trailer', 'Junkyard')
self.redis.lpush('bus_junkyard_trailer', 'Depot')
self.redis.lpush('bus_junkyard_trailer', 'Garbage Lot')
self.redis.lpush('bus_junkyard_trailer', 'Pile')
self.redis.lpush('bus_junkyard_trailer', 'Dumping Ground')
self.redis.lpush('bus_junkyard_trailer', 'Disposal Area')
self.redis.lpush('bus_junkyard_trailer', 'Waste Site')

########################################################
self.redis.lpush('business_kind', 'bus_lawenforcement')
SET   bus_lawenforcement_kindname law enforcement
SET   bus_lawenforcement_perbuilding 20

SET   bus_lawenforcement_maxfloors 2
SET   bus_lawenforcement_district civic

self.redis.lpush('bus_lawenforcement_manager', 'deputy')
self.redis.lpush('bus_lawenforcement_manager', 'sheriff')

self.redis.lpush('bus_lawenforcement_managerclass', 'commoner')
self.redis.lpush('bus_lawenforcement_managerclass', 'expert')

self.redis.lpush('bus_lawenforcement_service', 'service')

self.redis.lpush('bus_lawenforcement_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_leathershop')
SET   bus_leathershop_kindname leathershop
SET   bus_leathershop_perbuilding 10

SET   bus_leathershop_maxfloors 2
SET   bus_leathershop_district trade

self.redis.lpush('bus_leathershop_manager', 'leatherworker')

self.redis.lpush('bus_leathershop_managerclass', 'commoner')
self.redis.lpush('bus_leathershop_managerclass', 'expert')

self.redis.lpush('bus_leathershop_service', 'service')

self.redis.lpush('bus_leathershop_trailer', 'Leatherworks')

########################################################
self.redis.lpush('business_kind', 'bus_library')
SET   bus_library_kindname library
SET   bus_library_perbuilding 10

SET   bus_library_maxfloors 3
SET   bus_library_district fine shops

self.redis.lpush('bus_library_manager', 'librarian')
self.redis.lpush('bus_library_manager', 'sage')
self.redis.lpush('bus_library_manager', 'scribe')

self.redis.lpush('bus_library_managerclass', 'adept')
self.redis.lpush('bus_library_managerclass', 'commoner')
self.redis.lpush('bus_library_managerclass', 'expert')

self.redis.lpush('bus_library_service', 'service')
self.redis.lpush('bus_library_service', 'library cards')

self.redis.lpush('bus_library_trailer', 'Public Library')
self.redis.lpush('bus_library_trailer', 'Study')
self.redis.lpush('bus_library_trailer', 'Reference Center')

########################################################
self.redis.lpush('business_kind', 'bus_locksmith')
SET   bus_locksmith_kindname locksmith
SET   bus_locksmith_perbuilding 4

SET   bus_locksmith_maxfloors 1
SET   bus_locksmith_district trade

self.redis.lpush('bus_locksmith_manager', 'locksmith')

self.redis.lpush('bus_locksmith_managerclass', 'adept')
self.redis.lpush('bus_locksmith_managerclass', 'barbarian')
self.redis.lpush('bus_locksmith_managerclass', 'bard')
self.redis.lpush('bus_locksmith_managerclass', 'commoner')
self.redis.lpush('bus_locksmith_managerclass', 'expert')
self.redis.lpush('bus_locksmith_managerclass', 'rogue')

self.redis.lpush('bus_locksmith_service', 'service')
self.redis.lpush('bus_locksmith_service', 'new keys')
self.redis.lpush('bus_locksmith_service', 'new locks')
self.redis.lpush('bus_locksmith_service', 'lock repairs')

self.redis.lpush('bus_locksmith_trailer', 'Locksmith')

########################################################
self.redis.lpush('business_kind', 'bus_lumbermill')
SET   bus_lumbermill_kindname lumbermill
SET   bus_lumbermill_perbuilding 30

SET   bus_lumbermill_maxfloors 2
SET   bus_lumbermill_district industry

self.redis.lpush('bus_lumbermill_manager', 'lumberjack')

self.redis.lpush('bus_lumbermill_managerclass', 'commoner')

self.redis.lpush('bus_lumbermill_service', 'service')
self.redis.lpush('bus_lumbermill_service', 'timber')

self.redis.lpush('bus_lumbermill_trailer', 'Lumber Mill')
self.redis.lpush('bus_lumbermill_trailer', 'Saw Mill')
self.redis.lpush('bus_lumbermill_trailer', 'Timber Mill')

########################################################
self.redis.lpush('business_kind', 'bus_lumberyard')
SET   bus_lumberyard_kindname lumberyard
SET   bus_lumberyard_perbuilding 10

SET   bus_lumberyard_maxfloors 1
SET   bus_lumberyard_district industry

self.redis.lpush('bus_lumberyard_manager', 'woodseller')

self.redis.lpush('bus_lumberyard_managerclass', 'commoner')

self.redis.lpush('bus_lumberyard_service', 'service')
self.redis.lpush('bus_lumberyard_service', 'lumber')
self.redis.lpush('bus_lumberyard_service', 'boards')

self.redis.lpush('bus_lumberyard_trailer', 'Lumberyard')
self.redis.lpush('bus_lumberyard_trailer', 'Timberyard')

########################################################
self.redis.lpush('business_kind', 'bus_magicshop')
SET   bus_magicshop_kindname magic shop
SET   bus_magicshop_perbuilding 3

SET   bus_magicshop_maxfloors 2
SET   bus_magicshop_district fine shops

self.redis.lpush('bus_magicshop_manager', 'magic dealer')

self.redis.lpush('bus_magicshop_managerclass', 'adept')
self.redis.lpush('bus_magicshop_managerclass', 'aristocrat')
self.redis.lpush('bus_magicshop_managerclass', 'commoner')
self.redis.lpush('bus_magicshop_managerclass', 'expert')
self.redis.lpush('bus_magicshop_managerclass', 'rogue')
self.redis.lpush('bus_magicshop_managerclass', 'sorcerer')
self.redis.lpush('bus_magicshop_managerclass', 'wizard')

self.redis.lpush('bus_magicshop_service', 'service')
self.redis.lpush('bus_magicshop_service', 'scrolls')

self.redis.lpush('bus_magicshop_trailer', 'Boutique')
self.redis.lpush('bus_magicshop_trailer', 'Shoppe')
self.redis.lpush('bus_magicshop_trailer', 'Magic Shop')

########################################################
self.redis.lpush('business_kind', 'bus_masonry')
SET   bus_masonry_kindname masonry shop
SET   bus_masonry_perbuilding 20

SET   bus_masonry_maxfloors 1
SET   bus_masonry_district industry

self.redis.lpush('bus_masonry_manager', 'mason')

self.redis.lpush('bus_masonry_managerclass', 'commoner')

self.redis.lpush('bus_masonry_service', 'service')
self.redis.lpush('bus_masonry_service', 'bricks')
self.redis.lpush('bus_masonry_service', 'walls')
self.redis.lpush('bus_masonry_service', 'facades')

self.redis.lpush('bus_masonry_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_mercer')
SET   bus_mercer_kindname mercer
SET   bus_mercer_perbuilding 20

SET   bus_mercer_maxfloors 2
SET   bus_mercer_district trade

self.redis.lpush('bus_mercer_manager', 'mercer')

self.redis.lpush('bus_mercer_managerclass', 'aristocrat')
self.redis.lpush('bus_mercer_managerclass', 'commoner')
self.redis.lpush('bus_mercer_managerclass', 'expert')

self.redis.lpush('bus_mercer_service', 'service')
self.redis.lpush('bus_mercer_service', 'linen')
self.redis.lpush('bus_mercer_service', 'cloth')
self.redis.lpush('bus_mercer_service', 'silk')

self.redis.lpush('bus_mercer_trailer', 'Textiles')
self.redis.lpush('bus_mercer_trailer', 'Fabrics')
self.redis.lpush('bus_mercer_trailer', 'Cloth')

########################################################
self.redis.lpush('business_kind', 'bus_mill')
SET   bus_mill_kindname mill
SET   bus_mill_perbuilding 20

SET   bus_mill_maxfloors 3
SET   bus_mill_district industry

self.redis.lpush('bus_mill_manager', 'miller')

self.redis.lpush('bus_mill_managerclass', 'commoner')

self.redis.lpush('bus_mill_service', 'service')

self.redis.lpush('bus_mill_trailer', 'Millers')
self.redis.lpush('bus_mill_trailer', 'Mill')

########################################################
self.redis.lpush('business_kind', 'bus_postoffice')
SET   bus_postoffice_kindname post office
SET   bus_postoffice_perbuilding 10

SET   bus_postoffice_maxfloors 1
SET   bus_postoffice_district embassy

self.redis.lpush('bus_postoffice_manager', 'messenger')

self.redis.lpush('bus_postoffice_managerclass', 'commoner')

self.redis.lpush('bus_postoffice_service', 'service')
self.redis.lpush('bus_postoffice_service', 'postage')

self.redis.lpush('bus_postoffice_trailer', 'Mail Service')
self.redis.lpush('bus_postoffice_trailer', 'Postal Service')
self.redis.lpush('bus_postoffice_trailer', 'Package Delivery')

########################################################
self.redis.lpush('business_kind', 'bus_pottery')
SET   bus_pottery_kindname pottery
SET   bus_pottery_perbuilding 10

SET   bus_pottery_maxfloors 1
SET   bus_pottery_district trade

self.redis.lpush('bus_pottery_manager', 'potter')

self.redis.lpush('bus_pottery_managerclass', 'commoner')
self.redis.lpush('bus_pottery_managerclass', 'expert')

self.redis.lpush('bus_pottery_service', 'service')
self.redis.lpush('bus_pottery_service', 'pots')
self.redis.lpush('bus_pottery_service', 'mugs')
self.redis.lpush('bus_pottery_service', 'vases')
self.redis.lpush('bus_pottery_service', 'jugs')
self.redis.lpush('bus_pottery_service', 'ceramics')

self.redis.lpush('bus_pottery_trailer', 'Ceramics')
self.redis.lpush('bus_pottery_trailer', 'Pots')
self.redis.lpush('bus_pottery_trailer', 'Pottery House')

########################################################
self.redis.lpush('business_kind', 'bus_pursemaker')
SET   bus_pursemaker_kindname pursemaker
SET   bus_pursemaker_perbuilding 20

SET   bus_pursemaker_maxfloors 1
SET   bus_pursemaker_district trade

self.redis.lpush('bus_pursemaker_manager', 'pursemaker')

self.redis.lpush('bus_pursemaker_managerclass', 'commoner')
self.redis.lpush('bus_pursemaker_managerclass', 'expert')
self.redis.lpush('bus_pursemaker_managerclass', 'rogue')

self.redis.lpush('bus_pursemaker_service', 'service')
self.redis.lpush('bus_pursemaker_service', 'purses')
self.redis.lpush('bus_pursemaker_service', 'bags')

self.redis.lpush('bus_pursemaker_trailer', 'Purse Shop')
self.redis.lpush('bus_pursemaker_trailer', 'Bags')

########################################################
self.redis.lpush('business_kind', 'bus_roofer')
SET   bus_roofer_kindname roofer
SET   bus_roofer_perbuilding 20

SET   bus_roofer_maxfloors 1
SET   bus_roofer_district trade

self.redis.lpush('bus_roofer_manager', 'roofer')

self.redis.lpush('bus_roofer_managerclass', 'commoner')

self.redis.lpush('bus_roofer_service', 'service')
self.redis.lpush('bus_roofer_service', 'roofs')

self.redis.lpush('bus_roofer_trailer', 'Roofing')
self.redis.lpush('bus_roofer_trailer', 'Construction')

########################################################
self.redis.lpush('business_kind', 'bus_ropemaker')
SET   bus_ropemaker_kindname ropemaker
SET   bus_ropemaker_perbuilding 20

SET   bus_ropemaker_maxfloors 1
SET   bus_ropemaker_district industry

self.redis.lpush('bus_ropemaker_manager', 'ropemaker')

self.redis.lpush('bus_ropemaker_managerclass', 'commoner')

self.redis.lpush('bus_ropemaker_service', 'service')
self.redis.lpush('bus_ropemaker_service', 'ropes')

self.redis.lpush('bus_ropemaker_trailer', 'Ropes')

########################################################
self.redis.lpush('business_kind', 'bus_rugmaker')
SET   bus_rugmaker_kindname rugmaker
SET   bus_rugmaker_perbuilding 20

SET   bus_rugmaker_maxfloors 1
SET   bus_rugmaker_district industry

self.redis.lpush('bus_rugmaker_manager', 'rugmaker')

self.redis.lpush('bus_rugmaker_managerclass', 'commoner')

self.redis.lpush('bus_rugmaker_service', 'service')
self.redis.lpush('bus_rugmaker_service', 'rugs')
self.redis.lpush('bus_rugmaker_service', 'carpets')

self.redis.lpush('bus_rugmaker_trailer', 'Rug Shop')
self.redis.lpush('bus_rugmaker_trailer', 'Rugs')

########################################################
self.redis.lpush('business_kind', 'bus_scabbardmaker')
SET   bus_scabbardmaker_kindname scabbard maker
SET   bus_scabbardmaker_perbuilding 10

SET   bus_scabbardmaker_maxfloors 1
SET   bus_scabbardmaker_district trade

self.redis.lpush('bus_scabbardmaker_manager', 'scabbardmaker')

self.redis.lpush('bus_scabbardmaker_managerclass', 'commoner')
self.redis.lpush('bus_scabbardmaker_managerclass', 'expert')

self.redis.lpush('bus_scabbardmaker_service', 'service')
self.redis.lpush('bus_scabbardmaker_service', 'scabbards')
self.redis.lpush('bus_scabbardmaker_service', 'scabbard repairs')

self.redis.lpush('bus_scabbardmaker_trailer', 'Scabbards')
self.redis.lpush('bus_scabbardmaker_trailer', 'Sheath Store')

########################################################
self.redis.lpush('business_kind', 'bus_school')
SET   bus_school_kindname school
SET   bus_school_perbuilding 10

SET   bus_school_maxfloors 2
SET   bus_school_district education

self.redis.lpush('bus_school_manager', 'teacher')

self.redis.lpush('bus_school_managerclass', 'adept')
self.redis.lpush('bus_school_managerclass', 'aristocrat')
self.redis.lpush('bus_school_managerclass', 'bard')
self.redis.lpush('bus_school_managerclass', 'cleric')
self.redis.lpush('bus_school_managerclass', 'commoner')
self.redis.lpush('bus_school_managerclass', 'expert')
self.redis.lpush('bus_school_managerclass', 'monk')
self.redis.lpush('bus_school_managerclass', 'wizard')

self.redis.lpush('bus_school_service', 'service')
self.redis.lpush('bus_school_service', 'tuition')

self.redis.lpush('bus_school_trailer', 'Elementary School')
self.redis.lpush('bus_school_trailer', 'Primary School')
self.redis.lpush('bus_school_trailer', 'Secondary School')
self.redis.lpush('bus_school_trailer', 'High School')
self.redis.lpush('bus_school_trailer', 'Middle School')
self.redis.lpush('bus_school_trailer', 'Reform School')
self.redis.lpush('bus_school_trailer', 'Military School')

########################################################
self.redis.lpush('business_kind', 'bus_sculpting')
SET   bus_sculpting_kindname sculpting house
SET   bus_sculpting_perbuilding 10

SET   bus_sculpting_maxfloors 2
SET   bus_sculpting_district professional

self.redis.lpush('bus_sculpting_manager', 'sculptor')

self.redis.lpush('bus_sculpting_managerclass', 'commoner')
self.redis.lpush('bus_sculpting_managerclass', 'expert')

self.redis.lpush('bus_sculpting_service', 'service')
self.redis.lpush('bus_sculpting_service', 'busts')
self.redis.lpush('bus_sculpting_service', 'statues')

self.redis.lpush('bus_sculpting_trailer', 'Sculptures')
self.redis.lpush('bus_sculpting_trailer', 'Studio')

########################################################
self.redis.lpush('business_kind', 'bus_shipyard')
SET   bus_shipyard_kindname shipyard
SET   bus_shipyard_perbuilding 30

SET   bus_shipyard_maxfloors 1
SET   bus_shipyard_district port

self.redis.lpush('bus_shipyard_manager', 'shipwright')

self.redis.lpush('bus_shipyard_managerclass', 'commoner')
self.redis.lpush('bus_shipyard_managerclass', 'expert')

self.redis.lpush('bus_shipyard_service', 'service')

self.redis.lpush('bus_shipyard_trailer', 'Shipyard')
self.redis.lpush('bus_shipyard_trailer', 'Ship Repair')
self.redis.lpush('bus_shipyard_trailer', 'Dock Company')
self.redis.lpush('bus_shipyard_trailer', 'Dry Dock')

########################################################
self.redis.lpush('business_kind', 'bus_shoeshop')
SET   bus_shoeshop_kindname shoe shop
SET   bus_shoeshop_perbuilding 10

SET   bus_shoeshop_maxfloors 1
SET   bus_shoeshop_district trade

self.redis.lpush('bus_shoeshop_manager', 'shoemaker')

self.redis.lpush('bus_shoeshop_managerclass', 'commoner')
self.redis.lpush('bus_shoeshop_managerclass', 'expert')

self.redis.lpush('bus_shoeshop_service', 'service')
self.redis.lpush('bus_shoeshop_service', 'shoes')
self.redis.lpush('bus_shoeshop_service', 'boots')

self.redis.lpush('bus_shoeshop_trailer', 'Shoes')
self.redis.lpush('bus_shoeshop_trailer', 'Shoes Inc.')

self.redis.lpush('bus_shoeshop_smell', 'scent of leather')
self.redis.lpush('bus_shoeshop_smell', 'rhythmic grinding')

self.redis.lpush('bus_shoeshop_sound', 'silence')
self.redis.lpush('bus_shoeshop_sound', 'the work of shoes')
self.redis.lpush('bus_shoeshop_sound', 'a kitten mewing')

self.redis.lpush('bus_shoeshop_sight', 'old shoes and bit of leather')
self.redis.lpush('bus_shoeshop_sight', 'a kitten')

########################################################
self.redis.lpush('business_kind', 'bus_shop')
SET   bus_shop_kindname shop
SET   bus_shop_perbuilding 30

SET   bus_shop_maxfloors 3
SET   bus_shop_district trade

self.redis.lpush('bus_shop_manager', 'tinker')
self.redis.lpush('bus_shop_manager', 'plasterer')
self.redis.lpush('bus_shop_manager', 'seamstress')

self.redis.lpush('bus_shop_managerclass', 'commoner')
self.redis.lpush('bus_shop_managerclass', 'expert')

self.redis.lpush('bus_shop_service', 'service')

self.redis.lpush('bus_shop_trailer', 'Shop')
self.redis.lpush('bus_shop_trailer', 'Shoppe')
self.redis.lpush('bus_shop_trailer', 'Store')
self.redis.lpush('bus_shop_trailer', 'Outlet')

########################################################
self.redis.lpush('business_kind', 'bus_slaughterhouse')
SET   bus_slaughterhouse_kindname slaughterhouse
SET   bus_slaughterhouse_perbuilding 20

SET   bus_slaughterhouse_maxfloors 1
SET   bus_slaughterhouse_district trade

self.redis.lpush('bus_slaughterhouse_manager', 'chickenbutcher')

self.redis.lpush('bus_slaughterhouse_managerclass', 'commoner')
self.redis.lpush('bus_slaughterhouse_managerclass', 'expert')

self.redis.lpush('bus_slaughterhouse_service', 'service')

self.redis.lpush('bus_slaughterhouse_trailer', 'Kennels')
self.redis.lpush('bus_slaughterhouse_trailer', 'Farm')
self.redis.lpush('bus_slaughterhouse_trailer', 'Meats')
self.redis.lpush('bus_slaughterhouse_trailer', 'Butchery')
self.redis.lpush('bus_slaughterhouse_trailer', 'Stockyard')

########################################################
self.redis.lpush('business_kind', 'bus_smithy')
SET   bus_smithy_kindname smithy
SET   bus_smithy_perbuilding 5

SET   bus_smithy_maxfloors 1
SET   bus_smithy_district shop

self.redis.lpush('bus_smithy_manager', 'blacksmith')
self.redis.lpush('bus_smithy_manager', 'smith')
self.redis.lpush('bus_smithy_manager', 'specialty smith')

self.redis.lpush('bus_smithy_managerclass', 'commoner')
self.redis.lpush('bus_smithy_managerclass', 'expert')
self.redis.lpush('bus_smithy_managerclass', 'fighter')
self.redis.lpush('bus_smithy_managerclass', 'warrior')

self.redis.lpush('bus_smithy_service', 'service')
self.redis.lpush('bus_smithy_service', 'horseshoes')
self.redis.lpush('bus_smithy_service', 'armor repairs')

self.redis.lpush('bus_smithy_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_smokehouse')
SET   bus_smokehouse_kindname smokehouse
SET   bus_smokehouse_perbuilding 30

SET   bus_smokehouse_maxfloors 2
SET   bus_smokehouse_district industry

self.redis.lpush('bus_smokehouse_manager', 'salter')

self.redis.lpush('bus_smokehouse_managerclass', 'commoner')

self.redis.lpush('bus_smokehouse_service', 'service')

self.redis.lpush('bus_smokehouse_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_spicemerchant')
SET   bus_spicemerchant_kindname spicemerchant
SET   bus_spicemerchant_perbuilding 10

SET   bus_spicemerchant_maxfloors 1
SET   bus_spicemerchant_district market

self.redis.lpush('bus_spicemerchant_manager', 'spicemerchant')

self.redis.lpush('bus_spicemerchant_managerclass', 'aristocrat')
self.redis.lpush('bus_spicemerchant_managerclass', 'commoner')
self.redis.lpush('bus_spicemerchant_managerclass', 'expert')

self.redis.lpush('bus_spicemerchant_service', 'service')
self.redis.lpush('bus_spicemerchant_service', 'spices')

self.redis.lpush('bus_spicemerchant_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_stable')
SET   bus_stable_kindname stable
SET   bus_stable_perbuilding 5

SET   bus_stable_maxfloors 1
SET   bus_stable_district professional

self.redis.lpush('bus_stable_manager', 'ostler')
self.redis.lpush('bus_stable_manager', 'stablehand')

self.redis.lpush('bus_stable_managerclass', 'commoner')

self.redis.lpush('bus_stable_service', 'service')
self.redis.lpush('bus_stable_service', 'stables')

self.redis.lpush('bus_stable_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_studio')
SET   bus_studio_kindname studio
SET   bus_studio_perbuilding 20

SET   bus_studio_maxfloors 1
SET   bus_studio_district trade

self.redis.lpush('bus_studio_manager', 'painter')
self.redis.lpush('bus_studio_manager', 'artist')

self.redis.lpush('bus_studio_managerclass', 'aristocrat')
self.redis.lpush('bus_studio_managerclass', 'commoner')
self.redis.lpush('bus_studio_managerclass', 'expert')

self.redis.lpush('bus_studio_service', 'service')

self.redis.lpush('bus_studio_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_tackshop')
SET   bus_tackshop_kindname tack shop
SET   bus_tackshop_perbuilding 5

SET   bus_tackshop_maxfloors 1
SET   bus_tackshop_district trade

self.redis.lpush('bus_tackshop_manager', 'saddler')

self.redis.lpush('bus_tackshop_managerclass', 'commoner')
self.redis.lpush('bus_tackshop_managerclass', 'expert')

self.redis.lpush('bus_tackshop_service', 'service')

self.redis.lpush('bus_tackshop_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_tannery')
SET   bus_tannery_kindname tannery
SET   bus_tannery_perbuilding 10

SET   bus_tannery_maxfloors 1
SET   bus_tannery_district industry

self.redis.lpush('bus_tannery_manager', 'tanner')

self.redis.lpush('bus_tannery_managerclass', 'commoner')
self.redis.lpush('bus_tannery_managerclass', 'expert')

self.redis.lpush('bus_tannery_service', 'service')
self.redis.lpush('bus_tannery_service', 'leather')

self.redis.lpush('bus_tannery_trailer', 'inc.')

self.redis.lpush('bus_tannery_smell', 'leather')

self.redis.lpush('bus_tannery_sound', 'an odd thumping sound')

self.redis.lpush('bus_tannery_sight', 'skins stretching')

########################################################
self.redis.lpush('business_kind', 'bus_tavern')
SET   bus_tavern_kindname tavern
SET   bus_tavern_perbuilding 5

SET   bus_tavern_maxfloors 3
SET   bus_tavern_district market

self.redis.lpush('bus_tavern_manager', 'tavern keeper')

self.redis.lpush('bus_tavern_managerclass', 'commoner')

self.redis.lpush('bus_tavern_service', 'service')
self.redis.lpush('bus_tavern_service', 'drinks')
self.redis.lpush('bus_tavern_service', 'food')

self.redis.lpush('bus_tavern_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_theater')
SET   bus_theater_kindname theater
SET   bus_theater_perbuilding 10

SET   bus_theater_maxfloors 3
SET   bus_theater_district entertainment

self.redis.lpush('bus_theater_manager', 'actor')
self.redis.lpush('bus_theater_manager', 'entertainer')

self.redis.lpush('bus_theater_managerclass', 'commoner')
self.redis.lpush('bus_theater_managerclass', 'expert')

self.redis.lpush('bus_theater_service', 'service')
self.redis.lpush('bus_theater_service', 'tickets')

self.redis.lpush('bus_theater_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_tileshop')
SET   bus_tileshop_kindname tile shop
SET   bus_tileshop_perbuilding 10

SET   bus_tileshop_maxfloors 1
SET   bus_tileshop_district trade

self.redis.lpush('bus_tileshop_manager', 'tilemaker')

self.redis.lpush('bus_tileshop_managerclass', 'commoner')

self.redis.lpush('bus_tileshop_service', 'service')
self.redis.lpush('bus_tileshop_service', 'tiles')

self.redis.lpush('bus_tileshop_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_townhouse')
SET   bus_townhouse_kindname townhouse
SET   bus_townhouse_perbuilding 10

SET   bus_townhouse_maxfloors 2
SET   bus_townhouse_district hotel

self.redis.lpush('bus_townhouse_manager', 'maidservant')

self.redis.lpush('bus_townhouse_managerclass', 'commoner')

self.redis.lpush('bus_townhouse_service', 'service')

self.redis.lpush('bus_townhouse_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_tradingpost')
SET   bus_tradingpost_kindname trading post
SET   bus_tradingpost_perbuilding 10

SET   bus_tradingpost_maxfloors 2
SET   bus_tradingpost_district shop

self.redis.lpush('bus_tradingpost_manager', 'trader')

self.redis.lpush('bus_tradingpost_managerclass', 'commoner')
self.redis.lpush('bus_tradingpost_managerclass', 'expert')

self.redis.lpush('bus_tradingpost_service', 'service')

self.redis.lpush('bus_tradingpost_trailer', 'general store')
self.redis.lpush('bus_tradingpost_trailer', 'shop')
self.redis.lpush('bus_tradingpost_trailer', 'general goods')

########################################################
self.redis.lpush('business_kind', 'bus_translator')
SET   bus_translator_kindname translator
SET   bus_translator_perbuilding 20

SET   bus_translator_maxfloors 1
SET   bus_translator_district embassy

self.redis.lpush('bus_translator_manager', 'interpreter')

self.redis.lpush('bus_translator_managerclass', 'adept')
self.redis.lpush('bus_translator_managerclass', 'commoner')
self.redis.lpush('bus_translator_managerclass', 'expert')

self.redis.lpush('bus_translator_service', 'service')
self.redis.lpush('bus_translator_service', 'translations')

self.redis.lpush('bus_translator_trailer', 'translations')
self.redis.lpush('bus_translator_trailer', 'word smiths')
self.redis.lpush('bus_translator_trailer', 'shop')

########################################################
self.redis.lpush('business_kind', 'bus_transportation')
SET   bus_transportation_kindname transportation
SET   bus_transportation_perbuilding 3

SET   bus_transportation_maxfloors 1
SET   bus_transportation_district professional

self.redis.lpush('bus_transportation_manager', 'coach driver')

self.redis.lpush('bus_transportation_managerclass', 'commoner')

self.redis.lpush('bus_transportation_service', 'service')

self.redis.lpush('bus_transportation_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_university')
SET   bus_university_kindname university
SET   bus_university_perbuilding 20

SET   bus_university_maxfloors 3
SET   bus_university_district education

self.redis.lpush('bus_university_manager', 'professor')

self.redis.lpush('bus_university_managerclass', 'adept')
self.redis.lpush('bus_university_managerclass', 'aristocrat')
self.redis.lpush('bus_university_managerclass', 'commoner')
self.redis.lpush('bus_university_managerclass', 'wizard')

self.redis.lpush('bus_university_service', 'service')
self.redis.lpush('bus_university_service', 'tuition')

self.redis.lpush('bus_university_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_vineyard')
SET   bus_vineyard_kindname vineyard
SET   bus_vineyard_perbuilding 10

SET   bus_vineyard_maxfloors 1
SET   bus_vineyard_district professional

self.redis.lpush('bus_vineyard_manager', 'vintner')

self.redis.lpush('bus_vineyard_managerclass', 'commoner')
self.redis.lpush('bus_vineyard_managerclass', 'expert')

self.redis.lpush('bus_vineyard_service', 'service')
self.redis.lpush('bus_vineyard_service', 'grapes')
self.redis.lpush('bus_vineyard_service', 'wine')

self.redis.lpush('bus_vineyard_trailer', 'vinters')
self.redis.lpush('bus_vineyard_trailer', 'wine shoppe')
self.redis.lpush('bus_vineyard_trailer', 'vineyards')

########################################################
self.redis.lpush('business_kind', 'bus_wagonyard')
SET   bus_wagonyard_kindname wagon yard
SET   bus_wagonyard_perbuilding 20

SET   bus_wagonyard_maxfloors 1
SET   bus_wagonyard_district industry

self.redis.lpush('bus_wagonyard_manager', 'wagoneer')

self.redis.lpush('bus_wagonyard_managerclass', 'commoner')
self.redis.lpush('bus_wagonyard_managerclass', 'expert')

self.redis.lpush('bus_wagonyard_service', 'service')
self.redis.lpush('bus_wagonyard_service', 'wagons')

self.redis.lpush('bus_wagonyard_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_warehouse')
SET   bus_warehouse_kindname warehouse
SET   bus_warehouse_perbuilding 10

SET   bus_warehouse_maxfloors 2
SET   bus_warehouse_district warehouse

self.redis.lpush('bus_warehouse_manager', 'laborer')
self.redis.lpush('bus_warehouse_manager', 'teamster')
self.redis.lpush('bus_warehouse_manager', 'warehouse worker')

self.redis.lpush('bus_warehouse_managerclass', 'commoner')

self.redis.lpush('bus_warehouse_service', 'service')

self.redis.lpush('bus_warehouse_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_dock')
SET   bus_dock_kindname dock
SET   bus_dock_perbuilding 10

SET   bus_dock_maxfloors 1
SET   bus_dock_district docks

self.redis.lpush('bus_dock_manager', 'navigator')
self.redis.lpush('bus_dock_manager', 'teamster')
self.redis.lpush('bus_dock_manager', 'warehouse worker')

self.redis.lpush('bus_dock_managerclass', 'commoner')

self.redis.lpush('bus_dock_service', 'service')

self.redis.lpush('bus_dock_trailer', 'Dock')

########################################################
self.redis.lpush('business_kind', 'bus_weaponshop')
SET   bus_weaponshop_kindname weaponshop
SET   bus_weaponshop_perbuilding 10

SET   bus_weaponshop_maxfloors 1
SET   bus_weaponshop_district merchant

self.redis.lpush('bus_weaponshop_manager', 'weaponsmith')

self.redis.lpush('bus_weaponshop_managerclass', 'commoner')
self.redis.lpush('bus_weaponshop_managerclass', 'expert')
self.redis.lpush('bus_weaponshop_managerclass', 'fighter')
self.redis.lpush('bus_weaponshop_managerclass', 'rogue')
self.redis.lpush('bus_weaponshop_managerclass', 'warrior')

self.redis.lpush('bus_weaponshop_service', 'service')

self.redis.lpush('bus_weaponshop_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_weaver')
SET   bus_weaver_kindname weaver
SET   bus_weaver_perbuilding 10

SET   bus_weaver_maxfloors 1
SET   bus_weaver_district industry

self.redis.lpush('bus_weaver_manager', 'weaver')

self.redis.lpush('bus_weaver_managerclass', 'commoner')
self.redis.lpush('bus_weaver_managerclass', 'expert')

self.redis.lpush('bus_weaver_service', 'service')

self.redis.lpush('bus_weaver_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_winery')
SET   bus_winery_kindname winery
SET   bus_winery_perbuilding 10

SET   bus_winery_maxfloors 1
SET   bus_winery_district merchant

self.redis.lpush('bus_winery_manager', 'wine seller')

self.redis.lpush('bus_winery_managerclass', 'commoner')

self.redis.lpush('bus_winery_service', 'service')
self.redis.lpush('bus_winery_service', 'wine')

self.redis.lpush('bus_winery_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_woodshop')
SET   bus_woodshop_kindname woodshop
SET   bus_woodshop_perbuilding 10

SET   bus_woodshop_maxfloors 1
SET   bus_woodshop_district trade

self.redis.lpush('bus_woodshop_manager', 'woodworker')
self.redis.lpush('bus_woodshop_manager', 'woodcarver')

self.redis.lpush('bus_woodshop_managerclass', 'commoner')
self.redis.lpush('bus_woodshop_managerclass', 'expert')

self.redis.lpush('bus_woodshop_service', 'service')

self.redis.lpush('bus_woodshop_trailer', 'inc.')

########################################################
self.redis.lpush('business_kind', 'bus_sawmill')
SET   bus_sawmill_kindname sawmill
SET   bus_sawmill_perbuilding 10

SET   bus_sawmill_maxfloors 1
SET   bus_sawmill_district industry

self.redis.lpush('bus_sawmill_manager', 'forester')
self.redis.lpush('bus_sawmill_manager', 'carpenter')
self.redis.lpush('bus_sawmill_manager', 'timberwright')

self.redis.lpush('bus_sawmill_managerclass', 'commoner')

self.redis.lpush('bus_sawmill_service', 'service')

self.redis.lpush('bus_sawmill_trailer', 'inc.')

self.redis.lpush('bus_sawmill_smell', 'sawdust')

self.redis.lpush('bus_sawmill_sound', 'a naphtha powered buzzsaw')

self.redis.lpush('bus_sawmill_sight', 'stacks of wood')

########################################################
self.redis.lpush('business_kind', 'bus_workshop')
SET   bus_workshop_kindname workshop
SET   bus_workshop_perbuilding 10

SET   bus_workshop_maxfloors 2
SET   bus_workshop_district shop

self.redis.lpush('bus_workshop_manager', 'handyman')

self.redis.lpush('bus_workshop_managerclass', 'commoner')
self.redis.lpush('bus_workshop_managerclass', 'rogue')

self.redis.lpush('bus_workshop_service', 'service')

self.redis.lpush('bus_workshop_trailer', 'inc.')

self.redis.lpush('bus_workshop_smell', 'sawdust')

self.redis.lpush('bus_workshop_sound', 'hammering from the back')

self.redis.lpush('bus_workshop_sight', 'tools and bits of wood lying around')

