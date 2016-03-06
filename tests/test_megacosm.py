#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import megacosm
from flask.ext.testing import TestCase
import fakeredis
from flask import Flask


class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        megacosm.app.debug = False
        megacosm.app.server=fakeredis.FakeRedis()
        return app

    def setUp(self):
        self.app = megacosm.app.test_client()
        self.redis=megacosm.app.server

        self.redis.hset('armor_ability_description', 'shock', '{"name":"shock",        "description":"has a chance of stunning an attacker" }')
        self.redis.hset('armor_category_description', 'leatherarmor', '{"name":"leather armor",     "materialpart":"chest" }')
        self.redis.hset('armor_decoration_description', 'flames', '{"name":"flames",   "description":"streaks of red and yellow which glisten like flames"  }')
        self.redis.hset('armor_effect_description', 'muffled', '{"name":"muffled",          "description":"allows the wearer to move more quietly than otherwise possible" }')
        self.redis.hset('armor_flaw_description', 'dent', '{"name":"dent", "description":"" }')
        self.redis.hset('armor_material_description', 'coldiron', '{"name":"cold iron",       "description":"beautiful cold steel"    }')
        self.redis.hset('armor_visualcause_description', 'orc', '{"name":"orc",      "description":"exposed to orcs"         }')
        self.redis.hset('armor_visualeffect_description', 'sparkles', '{"name":"sparkles",    "description":"emits a faint sparkle"                   }')
        self.redis.hset('curse_kind_description', 'bezerker', '{"name":"bezerker", "description":"causes intermittent, uncontrollable rage in the victim"  }')
        self.redis.hset('deity_primarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
        self.redis.hset('deity_secondarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
        self.redis.hset('deity_vow_description', 'humility', '{"name":"Humility",         "description":"abstain from extolling your own virtues"}')
        self.redis.hset('flagcolor_description', 'black', '{"name":"black",             "hex":"#000000",  "verb":"destroy",    "adverb":"purposefully"     }')
        self.redis.hset('flagcolor_description', 'brown', '{"name":"brown",             "hex":"#663300",  "verb":"withstand",  "adverb":"solidly"          }')
        self.redis.hset('flagcolor_description', 'darkbrown', '{"name":"dark brown",        "hex":"#330000",  "verb":"balance",    "adverb":"naturally"        }')
        self.redis.hset('flagcolor_description', 'lightred', '{"name":"light red",         "hex":"#ff3333",  "verb":"cherish",    "adverb":"peacefully"       }')
        self.redis.hset('flagcolor_description', 'purple', '{"name":"purple",            "hex":"#660099",  "verb":"rule",       "adverb":"majestically"     }')
        self.redis.hset('flagcolor_description', 'red', '{"name":"red",               "hex":"#ff0000",  "verb":"expand",     "adverb":"gracefully"       }')
        self.redis.hset('flagcolor_description', 'verylightred', '{"name":"very light red",    "hex":"#ff6666",  "verb":"love",       "adverb":"lovingly"         }')
        self.redis.hset('flagcolor_description', 'white', '{"name":"white",             "hex":"#ffffff",  "verb":"perfect",    "adverb":"peacefully"       }')
        self.redis.hset('gem_kind_description', 'emerald', '{ "name":"emerald", "color":["green"] }')
        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.hset('govtcountry_govttype_description', 'absolutemonarchy', '{ "name":"absolute monarchy",            "description":"the monarch rules unhindered"  }')
        self.redis.hset('govtcountry_govttype_description', 'authoritarian', '{ "name":"authoritarian government",     "description":"state authority is imposed onto many aspects of citizens\' lives"  }')
        self.redis.hset('govtcountry_govttype_description', 'commonwealth', '{ "name":"commonwealth",                 "description":"state authority is founded on law and united by a compact of the people for the common good"  }')
        self.redis.hset('govtcountry_govttype_description', 'communist', '{ "name":"communist government",         "description":"the state plans and controls the economy and a single party holds power"  }')
        self.redis.hset('govtcountry_govttype_description', 'constitutional', '{ "name":"constitutional government",    "description":"an authoritative document sets forth the system of fundamental laws and limits of that government"  }')
        self.redis.hset('govtcountry_govttype_description', 'democracy', '{ "name":"democracy",                    "description":"the supreme power is retained by the people, but is exercised through a system of representation"  }')
        self.redis.hset('govtcountry_govttype_description', 'dictatorship', '{ "name":"dictatorship",                 "description":"the ruler or small clique wield absolute power (not restricted by a constitution or laws)"  }')
        self.redis.hset('govtcountry_govttype_description', 'ecclesiastical', '{ "name":"ecclesiastical government",    "description":"the government administrated by a church."  }')
        self.redis.hset('govtcountry_govttype_description', 'emirate', '{ "name":"emirate",                      "description":"the supreme power is in the hands of an emir, who may be an absolute overlord with constitutionally limited authority"  }')
        self.redis.hset('govtcountry_govttype_description', 'federation', '{ "name":"federation",                   "description":"sovereign power is formally divided between a central authority and a number of constituent regions"  }')
        self.redis.hset('govtcountry_govttype_description', 'monarchy', '{ "name":"monarchy",                     "description":"the supreme power is lodged in the hands of a monarch who reigns with constitutionally limited authority"  }')
        self.redis.hset('govtcountry_govttype_description', 'oligarchy', '{ "name":"oligarchy",                    "description":"control is exercised by a small group of individuals whose authority generally is based on wealth or power"  }')
        self.redis.hset('govtcountry_govttype_description', 'parliamentary', '{ "name":"parliamentary government",     "description":"members are nominated to their positions by a parliament and can be dissolved by the parliament if it can no longer function"  }')
        self.redis.hset('govtcountry_govttype_description', 'republic', '{ "name":"republic",                     "description":"the people\'s elected representatives, not the people themselves, vote on legislation."  }')
        self.redis.hset('govtcountry_govttype_description', 'theocracy', '{ "name":"theocracy",                    "description":"a deity is recognized as the supreme civil ruler, but the deity\'s laws are interpreted by ecclesiastical authorities"  }')
        self.redis.hset('govtcountry_govttype_description', 'totalitarian', '{ "name":"totalitarian government",      "description":"the government subordinates individuals by controlling all political and economic matters, as well as the attitudes, values, and beliefs"  }')
        self.redis.hset('leaderabsolutemonarchy_leader_description', 'king', '{ "male":"King",    "female":"Queen"     }')
        self.redis.hset('leader_kind_description', 'absolutemonarchy', '{ "scope":"country"   }')
        self.redis.hset('roguedungeonroom_kind_description', 'audiencechamber', '{ "name":"audience chamber",   "description":""   }')
        self.redis.lpush('armor_ability', 'shock')
        self.redis.lpush('armor_category', 'leatherarmor')
        self.redis.lpush('armor_decoration', 'flames')
        self.redis.lpush('armor_effect', 'muffled')
        self.redis.lpush('armor_flaw', 'dent')
        self.redis.lpush('armor_material', 'coldiron')
        self.redis.lpush('armor_name_template', '{{ params.effect_description["name"] }} {{ params.category_description["name"]}}{%if params.ability_description%} of {{params.ability_description["name"]}}{%endif%}')
        self.redis.lpush('armor_visualcause', 'orc')
        self.redis.lpush('armor_visualeffect', 'sparkles')
        self.redis.lpush('artwork_cloth_item', 'glove')
        self.redis.lpush('artwork_cloth_material', 'silk')
        self.redis.lpush('artwork_item_decoration', 'bear')
        self.redis.lpush('artwork_item', 'harp')
        self.redis.lpush('artwork_item_material', 'ivory')
        self.redis.lpush('artwork_jewelry', 'ring')
        self.redis.lpush('artwork_metal', 'bronze')
        self.redis.lpush('artwork_template', "a necklace of {{params.gem.size}} {{params.gem.kind_description['name']|pluralize(2)}}")
        self.redis.lpush('artwork_weapon', 'dagger')
        self.redis.lpush('bond_template', 'Bob accepted you despite obvious failings. Which failing was the hardest?')
        self.redis.lpush('bus_adventurersguild_manager', 'adventurer')
        self.redis.lpush('bus_adventurersguild_manager', 'mercenary')
        self.redis.lpush('business_condition', 'cluttered')
        self.redis.lpush('business_direction', 'west')
        self.redis.lpush('business_kind', 'bus_adventurersguild')
        self.redis.lpush('business_rooftype', 'slate')
        self.redis.lpush('business_shade', 'bright')
        self.redis.lpush('business_storefront', 'mud')
        self.redis.lpush('business_trouble', 'slumping sales')
        self.redis.lpush('business_windows', 'clean')
        self.redis.lpush('country_right', 'appointment')
        self.redis.lpush('cuisine_template', 'words go here.')
        self.redis.lpush('currency_back','dragon')
        self.redis.lpush('currency_edges','ridges')
        self.redis.lpush('currency_front',"man's face")
        self.redis.lpush('currency_material','wood')
        self.redis.lpush('currency_shape','square')
        self.redis.lpush( 'currency_template', "{{params.name['full']|article|title}} is {{params.weight['name'] | article}}, {{params.value['name']}} coin that is common in the {{params.scope['name']}}. It is {{params.size['name']}}, {{params.shape}}, and made of {{params.material}}. The coins are covered with {{params.detail['name']}} designs.")
        self.redis.lpush('curse_kind', 'bezerker')
        self.redis.lpush('curse_removal', 'performing an epic task')
        self.redis.lpush('curse_template', "The {{params.kind_description['name']|title}} Curse {{params.kind_description['description']}}, and can only be undone by {{params.removal}}. Untreated, the effects of the curse {{params.duration['name']}}.")
        self.redis.lpush('deity_favored_stat', 'piety')
        self.redis.lpush('deity_favored_weapon', 'bows')
        self.redis.lpush('deity_form', 'talking jackal')
        self.redis.lpush('deity_holysymbol', 'axe')
        self.redis.lpush('deity_holysymbol_type', 'rocking')
        self.redis.lpush('deity_primarycolor', 'aquamarine')
        self.redis.lpush('deity_secondarycolor', 'aquamarine')
        self.redis.lpush('deity_vow', 'humility')
        self.redis.lpush('deity_worship', 'supplication')
        self.redis.lpush('eventdisaster_variety', 'animal infestation')
        self.redis.lpush('eventfestival_variety', 'a trade')
        self.redis.lpush('event_kind', 'disaster')
        self.redis.lpush('event_template', "{{params.variety }} {{params.kind}}, which is {{params.magnitude['name']}} to the people in the area.")
        self.redis.lpush('flag_border_solid_size', '.01')
        self.redis.lpush('flagcolor', 'black')
        self.redis.lpush('flagcolor', 'brown')
        self.redis.lpush('flagcolor', 'darkbrown')
        self.redis.lpush('flagcolor', 'lightred')
        self.redis.lpush('flagcolor', 'purple')
        self.redis.lpush('flagcolor', 'red')
        self.redis.lpush('flagcolor', 'verylightred')
        self.redis.lpush('flagcolor', 'white')
        self.redis.lpush('flag_division_diagonal_direction', 'left-to-right')
        self.redis.lpush('flag_division_stripes_colorcount', '2')
        self.redis.lpush('flag_division_stripes_count', '3')
        self.redis.lpush('flag_division_stripes_side', 'horizontal')
        self.redis.lpush('flag_overlay_circle_outline', 'false')
        self.redis.lpush('flag_overlay_circle_outlinewidth', '5')
        self.redis.lpush('flag_overlay_circle_radius', '.333')
        self.redis.lpush('flag_overlay_circle_radiusdirection', 'vertical')
        self.redis.lpush('flag_overlay_circle_x', '-1')
        self.redis.lpush('flag_overlay_circle_y', '.75')
        self.redis.lpush('flag_overlay_cross_horlength', '0.5')
        self.redis.lpush('flag_overlay_cross_horpos', '0.33')
        self.redis.lpush('flag_overlay_cross_horwidth', '0.2')
        self.redis.lpush('flag_overlay_cross_vertwidth', '0.05')
        self.redis.lpush('flag_overlay_diamond_outline', 'true')
        self.redis.lpush('flag_overlay_quaddiag_side', 'south')
        self.redis.lpush('flag_overlay_rays_count', '5')
        self.redis.lpush('flag_overlay_rays_offset', '.05')
        self.redis.lpush('flag_overlay_rays_x', '.25')
        self.redis.lpush('flag_overlay_rays_y', '.25')
        self.redis.lpush('flag_overlay_slash_direction', 'left-to-right')
        self.redis.lpush('flag_overlay_slash_width', '0.15')
        self.redis.lpush('flag_overlay_stripe_count', '2')
        self.redis.lpush('flag_overlay_stripe_side', 'horizontal')
        self.redis.lpush('flag_overlay_x_outline', 'false')
        self.redis.lpush('flag_overlay_x_width', '0.15')
        self.redis.lpush('flag_shape_swallow_depth', '30')
        self.redis.lpush('flag_shape_tongued_count', '11')
        self.redis.lpush('flag_shape_tongued_depth', '0.2')
        self.redis.lpush('flag_shape_tongued_shape', 'scallop')
        self.redis.lpush('flag_symbol_circle_outline', 'true')
        self.redis.lpush('flag_symbol_circle_radius', '.25')
        self.redis.lpush('flag_symbol_circle_radiusdirection', 'vertical')
        self.redis.lpush('flag_symbol_circle_x', '.25')
        self.redis.lpush('flag_symbol_circle_y', '.5')
        self.redis.lpush('flag_symbol_letter_fontfamily', 'Verdana Bold Italic')
        self.redis.lpush('flag_symbol_letter_size', '.25')
        self.redis.lpush('flag_symbol_letter_x', '.5')
        self.redis.lpush('flag_symbol_letter_y', '.5')
        self.redis.lpush('flag_symbol_star_inset', '.25')
        self.redis.lpush('flag_symbol_star_points', '4')
        self.redis.lpush('flag_symbol_star_x', '.5')
        self.redis.lpush('flag_symbol_star_y', '.5')
        self.redis.lpush('gem_kind', 'emerald')
        self.redis.lpush('gem_template', 'A Gem Template')
        self.redis.lpush('geomorphdungeon_template', '"Geomorph template shouldn\'t be used."')
        self.redis.lpush('geomorph_type_0', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_1', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_2', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_3', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_4', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_5', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('gnome_covering','skin')
        self.redis.lpush('gnome_name_first_post', 'Tom')
        self.redis.lpush('gnome_name_last_pre', 'Gyro')
        self.redis.lpush('govtcountry_govttype', 'absolutemonarchy')
        self.redis.lpush('govt_kind', 'country')
        self.redis.lpush('jobposting_class', 'warrior')
        self.redis.lpush('jobposting_critter', 'carnivorous butterflies')
        self.redis.lpush('jobposting_detail', 'if intrigued')
        self.redis.lpush('jobposting_disclaimer', 'Length of job expected to be short.')
        self.redis.lpush('jobposting_duration', 'few weeks')
        self.redis.lpush('jobposting_favor', 'companion or two')
        self.redis.lpush('jobposting_hazardlocation', 'my business')
        self.redis.lpush('jobposting_hook', 'Looking for something new?')
        self.redis.lpush('jobposting_item', 'keg')
        self.redis.lpush('jobposting_magicuser', 'witch/warlock')
        self.redis.lpush('jobposting_payment', 'Will reward you with valuable information.')
        self.redis.lpush('jobposting_rarelanguage', 'abyssal')
        self.redis.lpush('jobposting_request', 'Wanted:')
        self.redis.lpush('jobposting_requirement', 'Serious inquiries only.')
        self.redis.lpush('jobposting_skill', 'boxing')
        self.redis.lpush('jobposting_subject', 'local lore')
        self.redis.lpush('jobposting_supplies', 'eye of newt')
        self.redis.lpush('jobposting_template', '{{params.npc.name["full"]}} has been kidnapped! Generous payment for safe return.')
        self.redis.lpush('jobposting_testitem', 'cheese')
        self.redis.lpush('jobposting_valuedpossession', 'house')
        self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
        self.redis.lpush('leader_kind', 'absolutemonarchy')
        self.redis.lpush('legend_ability', 'make someone speak the truth')
        self.redis.lpush('legend_abilitytype', 'capability')
        self.redis.lpush('legend_area', 'swamps')
        self.redis.lpush('legend_badaction', 'took a hostage and demanded a ransom')
        self.redis.lpush('legend_badfate', 'will be stricken blind')
        self.redis.lpush('legend_badguy', 'a {{params.badguytype}} named {{params.villain.name["full"]}}')
        self.redis.lpush('legend_badguytype', 'devil')
        self.redis.lpush('legend_bait', 'ask for your help')
        self.redis.lpush('legend_caughtfailing', 'didn\'t get close')
        self.redis.lpush('legend_chumps', 'the royals')
        self.redis.lpush('legend_detect', 'confront')
        self.redis.lpush('legend_drawn', 'and was drawn towards thieves')
        self.redis.lpush('legend_failedresolution', 'stop the {{params.badguytype}}')
        self.redis.lpush('legend_goodstart', 'thrived')
        self.redis.lpush('legend_goodstatus', 'quiet')
        self.redis.lpush('legend_hero', 'a {{params.npc.behavior}} {{params.npc.race}} named {{params.npc.name["full"]}}')
        self.redis.lpush('legend_lastseen', 'mysteriously disappeared')
        self.redis.lpush('legend_monster', 'old woman')
        self.redis.lpush('legend_object', 'bag of beans')
        self.redis.lpush('legend_planaction', 'by making a wager with {{params.villain.name["full"]}}')
        self.redis.lpush('legend_plan', 'the thought to slay the {{params.badguytype}}')
        self.redis.lpush('legend_reputation', 'possessed')
        self.redis.lpush('legend_results', 'tricked {{params.villain.name["full"]}}')
        self.redis.lpush('legend_stopit', 'unless you offer a sacrifice')
        self.redis.lpush('legend_storytime', 'In olden times')
        self.redis.lpush('legend_talent', 'a valiant knight')
        self.redis.lpush('legend_template', '{{params.storytime}}, {{params.badguytype |article }} named {{params.villain.name["full"]}} {{params.wander}} the {{params.area}} {{params.when}} {{params.drawn}}. {{params.who}} say that if you {{params.detect}} {{params.villain.sex["third-person"]}}, you {{params.badfate}} {{params.stopit}}.')
        self.redis.lpush('legend_trap', 'give you a gift if you are nice')
        self.redis.lpush('legend_victory', 'and rescued the hostages')
        self.redis.lpush('legend_virtue', 'never trusting another {{params.badguytype}}')
        self.redis.lpush('legend_wander', 'haunted')
        self.redis.lpush('legend_when', 'when the wind blows from the west')
        self.redis.lpush('legend_who', 'People')
        self.redis.lpush('magicitem_creator_template', '{{npc.race | article}} named {{npc.name["full"]}}')
        self.redis.lpush('magicitem_kind', 'armor')
        self.redis.lpush('magicitem_location', 'buried in a nest')
        self.redis.lpush('magicitem_vibe', 'gives you feelings of power')
        self.redis.lpush('magicitem_vibe_when', 'looking at')
        self.redis.lpush('misfire_template', '{{params.target}} grow a pair of small horns (2 in each) on the forehead, which contrasts with skin color.  A remove curse may remove them.')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('mundaneitem_kind', 'wool tunic')
        self.redis.lpush('name_businessroot','Axe')
        self.redis.lpush('name_businesstitle','Angry')
        self.redis.lpush('name_continentpost', 'ca')
        self.redis.lpush('name_continentpre', 'As')
        self.redis.lpush('name_continentroot', 'bar')
        self.redis.lpush('name_continenttitle', 'West')
        self.redis.lpush('name_countrypre','Af')
        self.redis.lpush('name_countryroot','kil')
        self.redis.lpush('name_countrytitle', 'Central')
        self.redis.lpush('name_currencypost','abbi')
        self.redis.lpush('name_currencypre','yua')
        self.redis.lpush('name_currencyroot','fel')
        self.redis.lpush('name_organizationpost', 'za')
        self.redis.lpush('name_organizationpre', 'Blood')
        self.redis.lpush('name_organizationroot', 'for')
        self.redis.lpush('name_organizationtrailer', 'Horsemen')
        self.redis.lpush('name_planetpost', 'ris')
        self.redis.lpush('name_planetpre', 'Ae')
        self.redis.lpush('name_planetroot', 'boo')
        self.redis.lpush('naturalresource_crop_name', 'crop')
        self.redis.lpush('naturalresource_crop_name_type', 'wild')
        self.redis.lpush('naturalresource_crop_product', 'cocoa beans')
        self.redis.lpush('naturalresource_kind', 'crop')
        self.redis.lpush('npc_attitude', 'apologetic')
        self.redis.lpush('npc_attitude', 'attentive')
        self.redis.lpush('npc_build', 'skinny')
        self.redis.lpush('npc_complexion', 'tanned')
        self.redis.lpush('npc_eye', 'close-set')
        self.redis.lpush('npc_height', 'short')
        self.redis.lpush('npc_mark', 'birth mark')
        self.redis.lpush('npc_mark_location', 'hand')
        self.redis.lpush('npc_marriagestatus', 'widowed')
        self.redis.lpush('npc_medical_condition', 'constipation')
        self.redis.lpush('npc_posessiondetail', 'was lost during the war')
        self.redis.lpush('npc_posession', 'map')
        self.redis.lpush('npc_race','gnome')
        self.redis.lpush('npc_regret', 'seriously injured a friend goofing around')
        self.redis.lpush('organization_identification', 'by a tattoo')
        self.redis.lpush('organization_kind', 'association')
        self.redis.lpush('organization_powertype', 'criminal')
        self.redis.lpush('organization_template', '{{params.leader.name["lastname"] or params.name["pre"]+params.name["root"] }}\'s {{params.kind|title}}')
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('portfolio_level',1)
        self.redis.lpush('portfolio_level',16)
        self.redis.lpush('portfolio_level',2)
        self.redis.lpush('portfolio_level',3)
        self.redis.lpush('portfolio_level',4)
        self.redis.lpush('resource_kind', 'naturalresource')
        self.redis.lpush('resource_template', '"{{params.place.name["full"]}} is known for its {{params.name_type}} {{params.name}} which {{params.method}} {{params.product}}. This resource is {{params.ubiquity["name"]}} to the region. Many consider the {{params.product}} {{params.utility["name"]}}, and are regardless seen as a {{params.value["name"]}} resource. Competition in the {{params.product}} market is {{params.competition["name"]}}, and the {{params.name}} resource as a whole are {{params.management["name"]}} managed."')
        self.redis.lpush('roguedungeonroom_kind', 'audiencechamber')
        self.redis.lpush('roguedungeon_theme', 'fortress')
        self.redis.lpush('rumor_belief', '{{params.believer}} wants to believe it.')
        self.redis.lpush('rumor_dangeroushobby',  'drunkenly arguing with people')
        self.redis.lpush('rumor_fearresult', 'fell to the ground, dead')
        self.redis.lpush('rumor_heardit', '{{params.source}} said')
        self.redis.lpush('rumor_location', 'old millhouse')
        self.redis.lpush('rumor_past',' last year')
        self.redis.lpush('rumor_scarything', 'dragon')
        self.redis.lpush('rumor_stealth', 'quietly')
        self.redis.lpush('rumor_template', '{{params.culprit}} {{params.stealth}} {{params.verbed}} {{params.victim}}{{params.past}}.')
        self.redis.lpush('rumor_truth', '(True.)')
        self.redis.lpush('rumor_verbed', 'maimed')
        self.redis.lpush('skin_skincolor','alabaster')
        self.redis.lpush('skin_skinkind', 'thick')
        self.redis.lpush('starposition', '{"name": "companion2",    "x":-150,    "y":-4,  "z":4  }' )
        self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }' )
        self.redis.lpush('street_kind', 'road')
        self.redis.lpush('street_material', 'pavingstone')
        self.redis.lpush('wanted_by', 'Regional Authorities')
        self.redis.lpush('wanted_condition', 'proof of death')
        self.redis.lpush('wanted_crime', 'Desecration')
        self.redis.lpush('wanted_headline', 'Notice:')
        self.redis.lpush('wanted_lastseen', 'underground')
        self.redis.lpush('wanted_reward', '10 gold')
        self.redis.lpush('wanted_title', '"Loathsome"')
        self.redis.lpush('wanted_warning', 'has killed before')
        self.redis.lpush('weather_cloud', 'cumulus')
        self.redis.lpush('weather_storm', 'downburst')
        self.redis.lpush('weather_time', 'in the early evening')
        self.redis.set('bus_adventurersguild_district', 'professional')
        self.redis.set('bus_adventurersguild_kindname', 'adventurers guild')
        self.redis.set('bus_adventurersguild_maxfloors', '2')
        self.redis.set('bus_adventurersguild_perbuilding', '30')
        self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
        self.redis.set('magicitem_curse_chance', '40')
        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
        self.redis.zadd('business_age', '{  "name":"old"          , "score":100  }',100)
        self.redis.zadd('business_neighborhood', '{ "name":"expensive",    "score":100 }',100)
        self.redis.zadd('business_neighborhood', '{ "name":"new",          "score":100  }', 100)
        self.redis.zadd('business_popularity', '{  "name":"is constantly crowded"                              , "score":100 }',100)
        self.redis.zadd('business_price', '{  "name":"very high"          , "score":100  }',100)
        self.redis.zadd('business_reputation', '{  "name":"being a pillar of the community"          , "score":100  }',100)
        self.redis.zadd('business_size', '{  "name":"vast"           , "score":100 }',100)
        self.redis.zadd('business_status', '{  "name":"booming",            "score":100 }',100)
        self.redis.zadd('continent_civilization', '{"name":"thriving"    ,  "score":100   }',100)
        self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
        self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }',100)
        self.redis.zadd('continent_size', '{"name":"massive",  "multiplier":2.0,  "score":100   }',100)
        self.redis.zadd('continent_technology', ' {"name":"Contemporary Age", "score":100   }',100)
        self.redis.zadd('country_age', '{ "name":"ancient",        "score":100    }', 100)
        self.redis.zadd('country_aggression', '{"name":"timid",        "score":100    }', 100)
        self.redis.zadd('country_approval', '{ "name":"revere",         "score":100    }', 100)
        self.redis.zadd('country_corruption', '{ "name":"incorruptible",   "score":100    }', 100)
        self.redis.zadd('country_economic', '{"name":"conservative",     "score":100   }', 100)
        self.redis.zadd('country_efficiency', '{ "name":"ruthlessly effective",               "score":100    }', 100)
        self.redis.zadd('country_influence', '{ "name":"thriving",              "score":100    }', 100)
        self.redis.zadd('country_military', '{"name":"bloodthirsty",         "score":100    }', 100)
        self.redis.zadd('country_regiondetails','{"name":"a single",     "score":100,  "mincount":1,   "maxcount":1   }',100)
        self.redis.zadd('country_regiondetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
        self.redis.zadd('country_reputation', '{"name":"revered",     "score":100    }', 100)
        self.redis.zadd('country_size', '{"name":"massive",  "mincities":100, "maxcities":200,     "score":100    }', 100)
        self.redis.zadd('country_size', '{"name":"micro",    "mincities":1,   "maxcities":2,       "score":100    }', 100)
        self.redis.zadd('country_social', '{"name":"authoritarian",       "score":100   }', 100)
        self.redis.zadd('country_theology', '{ "name":"is used to control the populace",                                       "score":100    }', 100)
        self.redis.zadd('country_unity', '{ "name":"rallies behind its leaders",                         "score":100    }', 100)
        self.redis.zadd('currency_amount','{ "name":"a large pile of",    "min":100,  "max":3000, "score":100 }',100)
        self.redis.zadd('currency_detail','{ "name":"unmistakable" , "score":100  }',100)
        self.redis.zadd('currency_scope','{ "name":"continent",   "score":100  }',100)
        self.redis.zadd('currency_size','{ "name":"giant (40mm )"    , "score":100 }',100)
        self.redis.zadd('currency_value','{ "name":"priceless",         "score":100  }',100)
        self.redis.zadd('currency_weight','{ "name":"hefty" , "score":100  }',100)
        self.redis.zadd('curse_duration','{"name":"last a lifetime",       "score":100 }', 100)
        self.redis.zadd('deity_age', '{"name":"original",  "score":100   }', 100)
        self.redis.zadd('deity_followercount', '{"name":"countless",  "score":100   }', 100)
        self.redis.zadd('deity_followerzeal', '{"name":"overzealous",  "score":100   }', 100)
        self.redis.zadd('deity_health', '{"name":"more popular than ever",     "score":100 }', 100)
        self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100, "points":21 }',100)
        self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100,"points":21 }', 100)
        self.redis.zadd('deity_jealousy', '{"name":"jealous",  "score":100   }', 100)
        self.redis.zadd('deity_organized', '{"name":"rigidly",         "score":100 }', 100)
        self.redis.zadd('deity_secrecy', '{"name":"pompous",       "score":100   }', 100)
        self.redis.zadd('deity_unity', '{"name":"unified",     "score":100 }', 100)
        self.redis.zadd('event_magnitude', '{  "name":"of dire importance",            "score":100      }', 100)
        self.redis.zadd('flag_border', '{ "name":"solid", "score":100  }', 100)
        self.redis.zadd('flag_division', '{ "name":"stripes", "score":100  }', 100)
        self.redis.zadd('flag_overlay', '{ "name":"rays", "score":100  }', 100)
        self.redis.zadd('flag_ratio', '{ "name":"2.55", "score":100  }', 100)
        self.redis.zadd('flag_shape', '{"name":"tongued",     "score":100   }', 100)
        self.redis.zadd('flag_symbol', '{ "name":"letter", "score":100  }', 100)
        self.redis.zadd('gem_amount',  '{ "name":"a single",  "min":1, "max":100, "score":100  }',100.0)
        self.redis.zadd('gem_quality',  '{ "name":"chipped", "score":100  }',100.0)
        self.redis.zadd('gem_saturation',  '{ "name":"blanched", "score":100  }',100.0)
        self.redis.zadd('gem_value',  '{ "name":"costly", "score":100  }',100.0)
        self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"80%",   "offset":0.8,  "score":100 }', 100)
        self.redis.zadd('geomorphdungeon_gridheight', '{"name":"4",    "tiles":4,    "score": 100  }', 100)
        self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"6",     "tiles":6,   "score": 100  }', 100)
        self.redis.zadd('geomorphdungeon_segmentation', '{"name":"all",        "solidchance":0,        "score": 100  }', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)
        self.redis.zadd('govt_age', '{ "name":"far longer than should be allowed", "score":100      }', 100)
        self.redis.zadd('govt_approval', '{ "name":"revered",                                    "score":100      }', 100)
        self.redis.zadd('govt_corruption', '{ "name":"incorruptible",                            "score":100      }', 100)
        self.redis.zadd('govt_efficiency', '{ "name":"ruthlessly effective",                     "score":100      }', 100)
        self.redis.zadd('govt_influence', '{ "name":"thriving",           "score":100       }', 100)
        self.redis.zadd('govt_opposition', '{ "name":"violent",    "score":100      }', 100)
        self.redis.zadd('govt_reputation', '{ "name":"revered",    "score":100      }', 100)
        self.redis.zadd('govt_theology', '{ "name":"is used to control the populace",                                    "score":100       }', 100)
        self.redis.zadd('govt_unity', '{ "name":"rallies behind its leaders",                       "score":100       }', 100)
        self.redis.zadd('magicitem_age', '{"name":"over a century ago",    "score":100 }', 100)
        self.redis.zadd('magicitem_quality', '{"name":"excellent","score":100 }', 100)
        self.redis.zadd('magicitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
        self.redis.zadd('magicitem_strength', '{"name":"powerful",     "score":100  }', 100)
        self.redis.zadd('magicitem_value', '{"name":"artifact",              "score": 100  }', 100)
        self.redis.zadd('moon_color', '{  "name":"dull brown", "color":"0x876e4b" , "score":100  }', 100)
        self.redis.zadd('moon_size', '{  "name":"massive", "multiplier":0.8 , "score":100  }', 100)
        self.redis.zadd('mundaneitem_quality', '{"name":"excellent","score":100 }', 100)
        self.redis.zadd('mundaneitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
        self.redis.zadd('npc_age', '{"name":"ancient",        "score":100 }', 100)
        self.redis.zadd('npc_agility', '{"name":"agile",   "score":100  }', 100)
        self.redis.zadd('npc_attractiveness', '{"name":"stunning",     "score":100 }', 100)
        self.redis.zadd('npc_bravery', '{"name":"heroic",   "score":100  }', 100)
        self.redis.zadd('npc_charisma', '{"name":"inspiring",   "score":100  }', 100)
        self.redis.zadd('npc_confident', '{"name":"incredibly",     "score":100 }', 100)
        self.redis.zadd('npc_endurance', '{"name":"unflagging",   "score":100  }', 100)
        self.redis.zadd('npc_experience', '{"name":"grizzled",   "score":100  }', 100)
        self.redis.zadd('npc_generous', '{"name":"generous",     "score":100 }', 100)
        self.redis.zadd('npc_honor', '{"name":"honorable",     "score":100 }', 100)
        self.redis.zadd('npc_intelligence', '{"name":"brilliant",   "score":100  }', 100)
        self.redis.zadd('npc_kill', '{"name":"killed without issue",             "score":100  }', 100)
        self.redis.zadd('npc_luck', '{"name":"lucky",          "score":100 }', 100)
        self.redis.zadd('npc_money', '{"name":"rich",             "score":100 }', 100)
        self.redis.zadd('npc_piety', '{"name":"overzealous",   "score":100   }', 100)
        self.redis.zadd('npc_satisfaction', '{"name":"satisfied",   "score":100  }', 100)
        self.redis.zadd('npc_sex', '{"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }', 100)
        self.redis.zadd('npc_skill', '{"name":"legendarily skilled",   "score":100  }', 100)
        self.redis.zadd('npc_strength', '{"name":"herculean",   "score":100  }', 100)
        self.redis.zadd('npc_wisdom', '{"name":"wise",   "score":100  }', 100)
        self.redis.zadd('organization_adaptability', '{"name":"stay ahead of new development",    "score":100  }', 100)
        self.redis.zadd('organization_age', '{"name":"ancient",       "score":100  }', 100)
        self.redis.zadd('organization_entry', '{"name":"impossible",      "score":100  }', 100)
        self.redis.zadd('organization_failure', '{ "name":"better guidance and training",  "score":100 }', 100)
        self.redis.zadd('organization_leadership', '{ "name":"strong",     "score":100 }', 100)
        self.redis.zadd('organization_legal', '{"name":"legitimate",   "score":100   }', 100)
        self.redis.zadd('organization_morale', '{"name":"encouraged",          "score":100  }', 100)
        self.redis.zadd('organization_regulation', '{ "name":"strictly enforced",  "score":100 }', 100)
        self.redis.zadd('organization_rules', '{ "name":"rigidly",    "score":100 }', 100)
        self.redis.zadd('organization_size', '{ "name":"world",       "score":100 }', 100)
        self.redis.zadd('organization_stability', '{ "name":"are rock solid",     "score":100 }', 100)
        self.redis.zadd('organization_structure', '{ "name":"rigidly",    "score":100 }', 100)
        self.redis.zadd('organization_teamwork', '{ "name":"as a well oiled machine",         "score":100 }', 100)
        self.redis.zadd('organization_violence', '{"name":"passive",       "score":100  }', 100)
        self.redis.zadd('organization_visibility', '{ "name":"well known",            "score":100 }', 100)

        #Details for Kobolds
        self.redis.set( 'kobold_details', '{"name": "Kobold",     "size": "small",   "description": "their small stature and cowardice"}') 
        self.redis.lpush('kobold_covering','skin') 
        self.redis.zadd('kobold_name_order','{ "name":"first" }',50) 
        self.redis.hset('kobold_name_first','root', 100) 
        self.redis.lpush('kobold_name_first_root', 'Kole') 
 
        self.redis.zadd('kobold_name_order','{ "name":"last" }',100) 
        self.redis.hset('kobold_name_last','root', 0) 
        self.redis.lpush('kobold_name_last_root', 'Sok') 
 
        self.redis.set('kobold_subrace_chance',100) 
        self.redis.lpush('kobold_subrace', 'aquatic') 
 
        self.redis.hset('kobold_subrace_description', 'aquatic', '{"subrace": "Aquatic Kobold",   "description": "" }') 

        self.redis.zadd('city_size', '{ "name":"capitol",       "minpop":"30001", "maxpop":"80000", "min_density":"240", "max_density":"40000", "min_dist":3,  "max_dist":14 }', 100)
        self.redis.zadd('city_happiness', ' { "name":"estatic",     "score":100   }', 100)
        self.redis.zadd('city_health', ' { "name":"vigorous",       "score":100   }', 100)
        self.redis.zadd('city_age', ' { "name":"ancient",           "score":100    }', 100)
        self.redis.zadd('city_terrain', '{ "name": "jagged",         "score":100   }', 100)
        self.redis.zadd('city_pollution', '{ "name": "squalid",      "score":100  }', 100)
        self.redis.zadd('city_moral', '{ "name": "virtuous",         "score":100   }', 100)
        self.redis.zadd('city_order', '{ "name": "honorable",         "score":100   }', 100)
        self.redis.zadd('city_tolerance', '{ "name": "love",                        "score":100   }', 100)
        self.redis.zadd('city_economy', '{ "name": "lively",                        "score":100   }', 100)
        self.redis.zadd('city_military', '{ "name": "reverent",                     "score":100   }', 100)
        self.redis.zadd('city_magic', '{ "name": "growing",                         "score":100   }', 100)
        self.redis.zadd('city_education', '{ "name": "wonderful",                   "score":100   }', 100)
        self.redis.zadd('city_authority', '{ "name": "is very authoritarian",       "score":100   }', 100)
        self.redis.zadd('city_crime', '{ "name": "unheard of",                      "score":100   }', 100)

        self.redis.lpush('city_shape', 'octagonal')
        self.redis.lpush('city_gatheringplace', 'adventurersguild')

        self.redis.zadd('planet_atmosphere', '{"name":"dense",    "opacity":0.99,  "score":100   } ', 100)
        self.redis.zadd('planet_civilization', '{"name":"thriving"    ,  "score":100   } ', 100)
        self.redis.zadd('planet_day', '{"name":"long",        "minhour":51,     "maxhour":100,  "score":100   } ', 100)
        self.redis.zadd('planet_mooncount','{"name":"no moons",     "count":0,  "score":100   }',100.0)
        self.redis.zadd('planet_mooncount', '{"name":"quadruple moon",   "count":4,  "score":100   } ', 100)
        self.redis.zadd('planet_precipitation', '{"name":"excessive", "multiplier":1.5 ,  "score":100   } ', 100)
        self.redis.zadd('planet_size', '{"name":"massive",  "multiplier":2.0,  "score":100   } ', 100)
        self.redis.zadd('planet_technology', '{"name":"Contemporary Age", "description":"being similar to our own",           "score":100   } ', 100)
        self.redis.zadd('planet_temp', '{"name":"unbearably hot",  "multiplier":1.5,  "score":100   } ', 100)
        self.redis.zadd('planet_wind', '{"name":"overwhelming", "multiplier":1.5,  "score":100   } ', 100)
        self.redis.zadd('planet_year', '{"name":"long"     ,  "score":100   } ', 100)
        self.redis.zadd('portfolio_domain', '{"name":"adventure",                       "score":1 }', 1)
        self.redis.zadd('portfolio_domain', '{"name":"cold",                       "score":4 }', 4)
        self.redis.zadd('portfolio_domain', '{"name":"good",                       "score":16 }', 16)
        self.redis.zadd('portfolio_domain', '{"name":"song",                       "score":2 }', 2)
        self.redis.zadd('portfolio_domain', '{"name":"zeal",                       "score":3 }', 3)
        self.redis.zadd('region_corruption', '{ "name":"incorruptible",   "score":100    }', 100)
        self.redis.zadd('region_countryapproval', '{ "name":"revere",         "score":100   }', 100)
        self.redis.zadd('region_economic', '{"name":"conservative",     "score":100   }', 100)
        self.redis.zadd('region_efficiency', '{ "name":"ruthlessly effective",               "score":100   }', 100)
        self.redis.zadd('region_influence', '{ "name":"thriving",              "score":100   }', 100)
        self.redis.zadd('region_size', '{"name":"large",    "mincities":5,   "maxcities":20,      "score":100   }', 100)
        self.redis.zadd('region_social', '{"name":"authoritarian",       "score":100   }', 100)
        self.redis.zadd('region_theology', '{ "name":"is used to control the populace",                                      "score":100    }', 100)
        self.redis.zadd('region_unity', '{ "name":"rallies behind its leaders",                         "score":100   }', 100)
        self.redis.zadd('resource_competition', '{  "name":"fierce",             "score":100      }', 100)
        self.redis.zadd('resource_depletion', '{  "name":"bountiful",           "score":100      }', 100)
        self.redis.zadd('resource_exportregion', '{  "name":"across the continent",           "score":100      }', 100)
        self.redis.zadd('resource_management', '{  "name":"well",           "score":100      }', 100)
        self.redis.zadd('resource_ubiquity', '{  "name":"not specific",       "score":100       }', 100)
        self.redis.zadd('resource_utility', '{  "name":"useful",          "score":100      }', 100)
        self.redis.zadd('resource_value', '{  "name":"valuable",          "score":100      }', 100)
        self.redis.zadd('roguedungeon_build', '{"name":"dungeon and caves",    "score": 100  }', 100)
        self.redis.zadd('roguedungeon_refinement', '{"name":"dungeon",                             "score": 100  }', 100)
        self.redis.zadd('roguedungeon_room_count', '{"name":"lots",       "minsize":25, "maxsize":50,  "score": 100  }', 100)
        self.redis.zadd('roguedungeon_room_size', '{"name":"gigantic", "minsize":3,  "maxsize":20,   "score": 100  }', 100)
        self.redis.zadd('roguedungeon_size', '{"name":"gigantic", "minsize":60, "maxsize":60,   "score": 100  }', 100)
        self.redis.zadd( 'sect_acceptance','{"name":"saintly",  "score":100   }',100)
        self.redis.zadd('star_color', '{ "name":"red",    "color":"0xff0000", "luminosity":0.2, "score":100  }', 100)
        self.redis.zadd('star_size', '{ "name":"massive",    "multiplier":3.0, "score":100  }', 100)
        self.redis.zadd('starsystem_starcount',  '{ "name":"binary star",  "count":2, "score":100  }',100.0)
        self.redis.zadd('street_age', '{ "name":"ancient",         "score":100   }', 100)
        self.redis.zadd('street_crime', '{"name":"unheard of",                                     "score":100  }', 100)
        self.redis.zadd('street_economy', '{"name":"lively",                                         "score":100  }', 100)
        self.redis.zadd('street_important', '{ "name":"primary",    "score":100   }', 100)
        self.redis.zadd('street_moral', '{"name":"virtuous",                                    "score":100  }', 100)
        self.redis.zadd('street_order', '{"name":"honorable",                                         "score":100  }', 100)
        self.redis.zadd('street_pollution', '{"name":"squalid",        "score":100 }', 100)
        self.redis.zadd('street_popularity', '{ "name":"popular",    "score":100   }', 100)
        self.redis.zadd('street_repair', '{ "name":"pristine",            "score":100   }', 100)
        self.redis.zadd('street_scope', '{ "name":"country",     "score":100   }', 100)
        self.redis.zadd('street_size', '{ "name":"wide",             "score":100   }', 100)
        self.redis.zadd('street_terrain', '{"name":"jagged",      "score":100 }', 100)
        self.redis.zadd('street_tolerance', '{"name":"love",                                         "score":100  }', 100)
        self.redis.zadd('weather_precipitation', '{ "name":"heavily",    "score":100     }', 100)
        self.redis.zadd('weather_temp', '{ "name":"unbearably hot",   "score":100     }', 100)
        self.redis.zadd('weather_wind', '{ "name":"hurricane-force",  "score":100     }', 100)

    def tearDown(self):
        megacosm.app.server.flushall()
        self.app = None

################################################################

    def test_builder_form_data(self):
        megacosm.app.server.lpush('unittestgenerator_list', 'a', 'b', 'c')
        megacosm.app.server.set('unittestgenerator_list_chance', 30)
        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test1"}', 50)
        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test2"}', 100)
        megacosm.app.server.hset('unittestgenerator_list_description', 'foo', '{"name":"test1"}')
        megacosm.app.server.hset('unittestgenerator_list-description', 'bar', '{"name":"test2"}')
        self.assertEquals(megacosm.builder_form_data('unittestgenerator'), ({'list': ['c', 'b', 'a']},
                          {'list_chance': '30'}, {'range': [{u'name': u'test1'}, {u'name': u'test2'}]}))

        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test2"', 100)

        with self.assertRaisesRegexp(ValueError, 'failed to parse unittestgenerator_range field {"name":"test2"'):
            megacosm.builder_form_data('unittestgenerator')

    def test_isvalidscore(self):
        self.assertTrue(megacosm.isvalidscore('100'))
        self.assertTrue(megacosm.isvalidscore('50'))
        self.assertTrue(megacosm.isvalidscore('0'))
        self.assertFalse(megacosm.isvalidscore('-10'))
        self.assertFalse(megacosm.isvalidscore('1010'))
        self.assertFalse(megacosm.isvalidscore('Fred'))
################################################################

    def test_select_uppercase(self):
        self.assertEquals('DOG', megacosm.select_uppercase('dog'))
        self.assertEquals('APPLE?', megacosm.select_uppercase('Apple?'))
        self.assertEquals('HOUR.!', megacosm.select_uppercase('HOUR.!'))

################################################################

    def test_select_article(self):
        self.assertEquals('a dog', megacosm.select_article('dog'))
        self.assertEquals('an apple', megacosm.select_article('apple'))
        self.assertEquals('an hour', megacosm.select_article('hour'))

################################################################

    def test_select_pluralize(self):
        self.assertEquals('dogs', megacosm.select_pluralize('dog', 0))
        self.assertEquals('dog', megacosm.select_pluralize('dog', 1))
        self.assertEquals('dogs', megacosm.select_pluralize('dog', 2))
        self.assertEquals('classes', megacosm.select_pluralize('class', 0))
        self.assertEquals('class', megacosm.select_pluralize('class', 1))
        self.assertEquals('classes', megacosm.select_pluralize('class', 2))

################################################################

    def test_select_conjunction(self):
        self.assertEquals('a', megacosm.select_conjunction(['a']))
        self.assertEquals('a and b', megacosm.select_conjunction(['a', 'b']))
        self.assertEquals('a, b, and c', megacosm.select_conjunction(['a', 'b', 'c']))
        self.assertEquals('a, b, c, and d', megacosm.select_conjunction(['a', 'b', 'c', 'd']))

################################################################

    def test_select_plural_verb(self):
        self.assertEquals('were', megacosm.select_plural_verb('was', 0))
        self.assertEquals('was', megacosm.select_plural_verb('was', 1))
        self.assertEquals('were', megacosm.select_plural_verb('was', 2))

################################################################

    def test_select_plural_adj(self):
        self.assertEquals('some', megacosm.select_plural_adj('a', 0))
        self.assertEquals('a', megacosm.select_plural_adj('a', 1))
        self.assertEquals('some', megacosm.select_plural_adj('a', 2))

        self.assertEquals('these', megacosm.select_plural_adj('this', 0))
        self.assertEquals('this', megacosm.select_plural_adj('this', 1))
        self.assertEquals('these', megacosm.select_plural_adj('this', 2))

        self.assertEquals('those', megacosm.select_plural_adj('that', 0))
        self.assertEquals('that', megacosm.select_plural_adj('that', 1))
        self.assertEquals('those', megacosm.select_plural_adj('that', 2))

        self.assertEquals('our', megacosm.select_plural_adj('my', 0))
        self.assertEquals('my', megacosm.select_plural_adj('my', 1))
        self.assertEquals('our', megacosm.select_plural_adj('my', 2))

################################################################

    def test_index_route(self):
        response = self.app.get('/')
        self.assertTemplateUsed('index.html')
        self.assert200(response)

###############################################################

    def test_bond_route(self):
        response = self.app.get('/bond')
        self.assert200(response)

    def test_bond_builder_route(self):
        response = self.app.get('/bond_builder')
        self.assert200(response)

################################################################

    def test_business_route(self):
        response = self.app.get('/business')
        self.assert200(response)

    def test_business_builder_route(self):
        response = self.app.get('/business_builder')
        self.assert200(response)
################################################################

    def test_city_route(self):
        response = self.app.get('/city')
        self.assert200(response)

    def test_city_builder_route(self):
        response = self.app.get('/city_builder')
        self.assert200(response)

################################################################

    def test_continent_route(self):
        response = self.app.get('/continent')
        self.assert200(response)

    def test_continent_builder_route(self):
        response = self.app.get('/continent_builder')
        self.assert200(response)

################################################################

    def test_country_route(self):
        response = self.app.get('/country')
        self.assert200(response)

    def test_country_builder_route(self):
        response = self.app.get('/country_builder')
        self.assert200(response)

################################################################

    def test_cuisine_route(self):
        response = self.app.get('/cuisine')
        self.assert200(response)

    def test_cuisine_builder_route(self):
        response = self.app.get('/cuisine_builder')
        self.assert200(response)

################################################################

    def test_currency_route(self):
        response = self.app.get('/currency')
        self.assert200(response)

    def test_currency_builder_route(self):
        response = self.app.get('/currency_builder')
        self.assert200(response)

################################################################

    def test_deity_route(self):
        response = self.app.get('/deity')
        self.assert200(response)

    def test_deity_builder_route(self):
        response = self.app.get('/deity_builder')
        self.assert200(response)

################################################################

    def test_event_route(self):
        response = self.app.get('/event')
        self.assert200(response)

    def test_event_builder_route(self):
        response = self.app.get('/event_builder')
        self.assert200(response)

################################################################

    def test_flag_route(self):
        response = self.app.get('/flag')
        self.assert200(response)

    def test_flag_builder_route(self):
        response = self.app.get('/flag_builder')
        self.assert200(response)

################################################################

    def test_gem_route(self):
        response = self.app.get('/gem')
        self.assert200(response)

    def test_gem_builder_route(self):
        response = self.app.get('/gem_builder')
        self.assert200(response)

################################################################

    def test_geomorphdungeon_route(self):
        response = self.app.get('/geomorphdungeon')
        self.assert200(response)

    def test_geomorphdungeon_builder_route(self):
        response = self.app.get('/geomorphdungeon_builder')
        self.assert200(response)

################################################################

    def test_govt_route(self):
        response = self.app.get('/govt')
        self.assert200(response)

    def test_govt_builder_route(self):
        response = self.app.get('/govt_builder')
        self.assert200(response)

################################################################

    def test_jobposting_route(self):
        response = self.app.get('/jobposting')
        self.assert200(response)

    def test_jobposting_builder_route(self):
        response = self.app.get('/jobposting_builder')
        self.assert200(response)

################################################################

    def test_leader_route(self):
        response = self.app.get('/leader')
        self.assert200(response)

    def test_leader_builder_route(self):
        response = self.app.get('/leader_builder')
        self.assert200(response)

################################################################

    def test_legend_route(self):
        response = self.app.get('/legend')
        self.assert200(response)

    def test_legend_builder_route(self):
        response = self.app.get('/legend_builder')
        self.assert200(response)

################################################################

    def test_magicitem_route(self):
        response = self.app.get('/magicitem')
        self.assert200(response)

    def test_magicitem_builder_route(self):
        response = self.app.get('/magicitem_builder')
        self.assert200(response)

################################################################

    def test_misfire_route(self):
        response = self.app.get('/misfire')
        self.assert200(response)

    def test_misfire_builder_route(self):
        response = self.app.get('/misfire_builder')
        self.assert200(response)

################################################################

    def test_moon_route(self):
        response = self.app.get('/moon')
        self.assert200(response)

    def test_moon_builder_route(self):
        response = self.app.get('/moon_builder')
        self.assert200(response)

################################################################

    def test_motivation_route(self):
        response = self.app.get('/motivation')
        self.assert200(response)

    def test_motivation_builder_route(self):
        response = self.app.get('/motivation_builder')
        self.assert200(response)

################################################################

    def test_organization_route(self):
        response = self.app.get('/organization')
        self.assert200(response)

    def test_organization_builder_route(self):
        response = self.app.get('/organization_builder')
        self.assert200(response)

################################################################

    def test_phobia_route(self):
        response = self.app.get('/phobia')
        self.assert200(response)

    def test_phobia_builder_route(self):
        response = self.app.get('/phobia_builder')
        self.assert200(response)

################################################################

    def test_mundaneitem_route(self):
        response = self.app.get('/mundaneitem')
        self.assert200(response)

    def test_mundaneitem_builder_route(self):
        response = self.app.get('/mundaneitem_builder')
        self.assert200(response)

################################################################

    def test_npc_route(self):
        response = self.app.get('/npc')
        self.assert200(response)

    def test_npc_builder_route(self):
        response = self.app.get('/npc_builder')
        self.assert200(response)

################################################################

    def test_planet_route(self):
        response = self.app.get('/planet')
        self.assert200(response)

    def test_planet_builder_route(self):
        response = self.app.get('/planet_builder')
        self.assert200(response)

################################################################

    def test_region_route(self):
        response = self.app.get('/region')
        self.assert200(response)

    def test_region_builder_route(self):
        response = self.app.get('/region_builder')
        self.assert200(response)

################################################################

    def test_resource_route(self):
        response = self.app.get('/resource')
        self.assert200(response)

    def test_resource_builder_route(self):
        response = self.app.get('/resource_builder')
        self.assert200(response)

################################################################

    def test_roguedungeon_route(self):
        response = self.app.get('/roguedungeon')
        self.assert200(response)

    def test_roguedungeon_builder_route(self):
        response = self.app.get('/roguedungeon_builder')
        self.assert200(response)

################################################################

    def test_rumor_route(self):
        response = self.app.get('/rumor')
        self.assert200(response)

    def test_rumor_builder_route(self):
        response = self.app.get('/rumor_builder')
        self.assert200(response)

################################################################

    def test_sect_route(self):
        response = self.app.get('/sect')
        self.assert200(response)

    def test_sect_builder_route(self):
        response = self.app.get('/sect_builder')
        self.assert200(response)

################################################################

    def test_star_route(self):
        response = self.app.get('/star')
        self.assert200(response)

    def test_star_builder_route(self):
        response = self.app.get('/star_builder')
        self.assert200(response)

################################################################

    def test_street_route(self):
        response = self.app.get('/street')
        self.assert200(response)

    def test_street_builder_route(self):
        response = self.app.get('/street_builder')
        self.assert200(response)

################################################################

    def test_wanted_route(self):
        response = self.app.get('/wanted')
        self.assert200(response)

    def test_wanted_builder_route(self):
        response = self.app.get('/wanted_builder')
        self.assert200(response)

################################################################

    def test_weather_route(self):
        response = self.app.get('/weather')
        self.assert200(response)

    def test_weather_builder_route(self):
        response = self.app.get('/weather_builder')
        self.assert200(response)
################################################################

    def test_404_route(self):
        response = self.app.get('/brokenroute')
        self.assert404(response)

################################################################
    def test_feature_filter_npc(self):
        response = self.app.get('/npc?npc_endurance_roll=100&npc_medical_condition=0')
        self.assert200(response)

    def test_feature_filter_business(self):
        response = self.app.get('/business?business_kind=bus_adventurersguild')
        self.assert200(response)
        response = self.app.get('/business?business_kind=nothingcorrect')
        self.assert200(response)
        response = self.app.get('/business?business_kind=@@@')
        self.assert200(response)
        response = self.app.get('/business?business_kindof=bogus')
        self.assert200(response)


