
self.redis.lpush('phobia_template', 'You have {{params.strength[\'name\']}} {{params.kind_description[\'name\']}}, which is a fear of {{params.kind_description[\'description\']}}.')


ZADD phobia_strength  60 {"name":"mild",      "score":60    }
ZADD phobia_strength  80 {"name":"moderate",  "score":80    }
ZADD phobia_strength  90 {"name":"severe",    "score":90    }
ZADD phobia_strength 100 {"name":"crippling", "score":100   }


self.redis.lpush('phobia_kind', 'ablutophobia')
self.redis.lpush('phobia_kind', 'acarophobia')
self.redis.lpush('phobia_kind', 'acerophobia')
self.redis.lpush('phobia_kind', 'acousticophobia')
self.redis.lpush('phobia_kind', 'acrophobia')
self.redis.lpush('phobia_kind', 'aeroacrophobia')
self.redis.lpush('phobia_kind', 'aeronausiphobia')
self.redis.lpush('phobia_kind', 'aerophobia')
self.redis.lpush('phobia_kind', 'agoraphobia')
self.redis.lpush('phobia_kind', 'agrizoophobia')
self.redis.lpush('phobia_kind', 'agyrophobia')
self.redis.lpush('phobia_kind', 'aibohphobia')
self.redis.lpush('phobia_kind', 'aichmophobia')
self.redis.lpush('phobia_kind', 'albuminurophobia')
self.redis.lpush('phobia_kind', 'alektorophobia')
self.redis.lpush('phobia_kind', 'alliumphobia')
self.redis.lpush('phobia_kind', 'allodoxaphobia')
self.redis.lpush('phobia_kind', 'altophobia')
self.redis.lpush('phobia_kind', 'amaxophobia')
self.redis.lpush('phobia_kind', 'ambulophobia')
self.redis.lpush('phobia_kind', 'amnesiphobia')
self.redis.lpush('phobia_kind', 'amychophobia')
self.redis.lpush('phobia_kind', 'anablephobia')
self.redis.lpush('phobia_kind', 'ancraophobia')
self.redis.lpush('phobia_kind', 'androphobia')
self.redis.lpush('phobia_kind', 'anemophobia')
self.redis.lpush('phobia_kind', 'anginophobia')
self.redis.lpush('phobia_kind', 'angrophobia')
self.redis.lpush('phobia_kind', 'ankylophobia')
self.redis.lpush('phobia_kind', 'anthrophobia')
self.redis.lpush('phobia_kind', 'anthropophobia')
self.redis.lpush('phobia_kind', 'antlophobia')
self.redis.lpush('phobia_kind', 'anuptaphobia')
self.redis.lpush('phobia_kind', 'apeirophobia')
self.redis.lpush('phobia_kind', 'aphephobia')
self.redis.lpush('phobia_kind', 'apiphobia')
self.redis.lpush('phobia_kind', 'apotemnophobia')
self.redis.lpush('phobia_kind', 'aquaphobia')
self.redis.lpush('phobia_kind', 'arachibutyrophobia')
self.redis.lpush('phobia_kind', 'arachnophobia')
self.redis.lpush('phobia_kind', 'arithmophobia')
self.redis.lpush('phobia_kind', 'arsonphobia')
self.redis.lpush('phobia_kind', 'asthenophobia')
self.redis.lpush('phobia_kind', 'astraphobia')
self.redis.lpush('phobia_kind', 'astrapophobia')
self.redis.lpush('phobia_kind', 'astrophobia')
self.redis.lpush('phobia_kind', 'asymmetriphobia')
self.redis.lpush('phobia_kind', 'ataxiophobia')
self.redis.lpush('phobia_kind', 'ataxophobia')
self.redis.lpush('phobia_kind', 'atelophobia')
self.redis.lpush('phobia_kind', 'atephobia')
self.redis.lpush('phobia_kind', 'athazagoraphobia')
self.redis.lpush('phobia_kind', 'atychiphobia')
self.redis.lpush('phobia_kind', 'aulophobia')
self.redis.lpush('phobia_kind', 'aurophobia')
self.redis.lpush('phobia_kind', 'auroraphobia')
self.redis.lpush('phobia_kind', 'autodysomophobia')
self.redis.lpush('phobia_kind', 'automatonophobia')
self.redis.lpush('phobia_kind', 'automysophobia')
self.redis.lpush('phobia_kind', 'autophobia')
self.redis.lpush('phobia_kind', 'aviophobia')
self.redis.lpush('phobia_kind', 'bacillophobia')
self.redis.lpush('phobia_kind', 'ballistophobia')
self.redis.lpush('phobia_kind', 'barophobia')
self.redis.lpush('phobia_kind', 'basiphobia')
self.redis.lpush('phobia_kind', 'bathmophobia')
self.redis.lpush('phobia_kind', 'bathophobia')
self.redis.lpush('phobia_kind', 'batophobia')
self.redis.lpush('phobia_kind', 'batrachophobia')
self.redis.lpush('phobia_kind', 'belomophobia')
self.redis.lpush('phobia_kind', 'bibliophobia')
self.redis.lpush('phobia_kind', 'bogyphobia')
self.redis.lpush('phobia_kind', 'botanophobia')
self.redis.lpush('phobia_kind', 'bromidrophobia')
self.redis.lpush('phobia_kind', 'brontophobia')
self.redis.lpush('phobia_kind', 'bufonophobia')
self.redis.lpush('phobia_kind', 'cacomorphobia')
self.redis.lpush('phobia_kind', 'cacophobia')
self.redis.lpush('phobia_kind', 'cainophobia')
self.redis.lpush('phobia_kind', 'cainotophobia')
self.redis.lpush('phobia_kind', 'carcinophobia')
self.redis.lpush('phobia_kind', 'cardiophobia')
self.redis.lpush('phobia_kind', 'carnophobia')
self.redis.lpush('phobia_kind', 'catagelophobia')
self.redis.lpush('phobia_kind', 'catapedaphobia')
self.redis.lpush('phobia_kind', 'cathisophobia')
self.redis.lpush('phobia_kind', 'catoptrophobia')
self.redis.lpush('phobia_kind', 'cenophobia')
self.redis.lpush('phobia_kind', 'centophobia')
self.redis.lpush('phobia_kind', 'ceraunophobia')
self.redis.lpush('phobia_kind', 'chemophobia')
self.redis.lpush('phobia_kind', 'cherophobia')
self.redis.lpush('phobia_kind', 'chinophobia')
self.redis.lpush('phobia_kind', 'chiraptophobia')
self.redis.lpush('phobia_kind', 'chirophobia')
self.redis.lpush('phobia_kind', 'chiroptophobia')
self.redis.lpush('phobia_kind', 'cholerophobia')
self.redis.lpush('phobia_kind', 'chorophobia')
self.redis.lpush('phobia_kind', 'chrometophobia')
self.redis.lpush('phobia_kind', 'chromophobia')
self.redis.lpush('phobia_kind', 'chronomentrophobia')
self.redis.lpush('phobia_kind', 'chronophobia')
self.redis.lpush('phobia_kind', 'cibophobia')
self.redis.lpush('phobia_kind', 'claustrophobia')
self.redis.lpush('phobia_kind', 'cleithrophobia')
self.redis.lpush('phobia_kind', 'climacophobia')
self.redis.lpush('phobia_kind', 'clinophobia')
self.redis.lpush('phobia_kind', 'cnidophobia')
self.redis.lpush('phobia_kind', 'coimetrophobia')
self.redis.lpush('phobia_kind', 'cometophobia')
self.redis.lpush('phobia_kind', 'consecotaleophobia')
self.redis.lpush('phobia_kind', 'coprastasophobia')
self.redis.lpush('phobia_kind', 'coulrophobia')
self.redis.lpush('phobia_kind', 'cremnophobia')
self.redis.lpush('phobia_kind', 'cryophobia')
self.redis.lpush('phobia_kind', 'crystallophobia')
self.redis.lpush('phobia_kind', 'cyclophobia')
self.redis.lpush('phobia_kind', 'cynophobia')
self.redis.lpush('phobia_kind', 'daemonophobia')
self.redis.lpush('phobia_kind', 'decidophobia')
self.redis.lpush('phobia_kind', 'deipnophobia')
self.redis.lpush('phobia_kind', 'dementophobia')
self.redis.lpush('phobia_kind', 'demonophobia')
self.redis.lpush('phobia_kind', 'demophobia')
self.redis.lpush('phobia_kind', 'dendrophobia')
self.redis.lpush('phobia_kind', 'dermatopathophobia')
self.redis.lpush('phobia_kind', 'dermatophobia')
self.redis.lpush('phobia_kind', 'dextrophobia')
self.redis.lpush('phobia_kind', 'diabetophobia')
self.redis.lpush('phobia_kind', 'didaskaleinophobia')
self.redis.lpush('phobia_kind', 'dikephobia')
self.redis.lpush('phobia_kind', 'dinophobia')
self.redis.lpush('phobia_kind', 'diplophobia')
self.redis.lpush('phobia_kind', 'dipsophobia')
self.redis.lpush('phobia_kind', 'dishabiliophobia')
self.redis.lpush('phobia_kind', 'disposophobia')
self.redis.lpush('phobia_kind', 'domatophobia')
self.redis.lpush('phobia_kind', 'doraphobia')
self.redis.lpush('phobia_kind', 'doxophobia')
self.redis.lpush('phobia_kind', 'dysmorphophobia')
self.redis.lpush('phobia_kind', 'dystychiphobia')
self.redis.lpush('phobia_kind', 'ecclesiophobia')
self.redis.lpush('phobia_kind', 'ecophobia')
self.redis.lpush('phobia_kind', 'eisoptrophobia')
self.redis.lpush('phobia_kind', 'electrophobia')
self.redis.lpush('phobia_kind', 'eleutherophobia')
self.redis.lpush('phobia_kind', 'emetophobia')
self.redis.lpush('phobia_kind', 'enetophobia')
self.redis.lpush('phobia_kind', 'enosiophobia')
self.redis.lpush('phobia_kind', 'entomophobia')
self.redis.lpush('phobia_kind', 'eosophobia')
self.redis.lpush('phobia_kind', 'ephebiphobia')
self.redis.lpush('phobia_kind', 'epistaxiophobia')
self.redis.lpush('phobia_kind', 'epistemophobia')
self.redis.lpush('phobia_kind', 'equinophobia')
self.redis.lpush('phobia_kind', 'eremophobia')
self.redis.lpush('phobia_kind', 'ereuthophobia')
self.redis.lpush('phobia_kind', 'ereuthrophobia')
self.redis.lpush('phobia_kind', 'ergasiophobia')
self.redis.lpush('phobia_kind', 'ergophobia')
self.redis.lpush('phobia_kind', 'erythrophobia')
self.redis.lpush('phobia_kind', 'euphobia')
self.redis.lpush('phobia_kind', 'felinophobia')
self.redis.lpush('phobia_kind', 'frigophobia')
self.redis.lpush('phobia_kind', 'gametophobia')
self.redis.lpush('phobia_kind', 'geliophobia')
self.redis.lpush('phobia_kind', 'gelotophobia')
self.redis.lpush('phobia_kind', 'geniophobia')
self.redis.lpush('phobia_kind', 'genuphobia')
self.redis.lpush('phobia_kind', 'gephyrophobia')
self.redis.lpush('phobia_kind', 'gerascophobia')
self.redis.lpush('phobia_kind', 'gerontophobia')
self.redis.lpush('phobia_kind', 'geumophobia')
self.redis.lpush('phobia_kind', 'glossophobia')
self.redis.lpush('phobia_kind', 'graphophobia')
self.redis.lpush('phobia_kind', 'gynophobia')
self.redis.lpush('phobia_kind', 'haemaphobia')
self.redis.lpush('phobia_kind', 'haematophobia')
self.redis.lpush('phobia_kind', 'hagiophobia')
self.redis.lpush('phobia_kind', 'hamartophobia')
self.redis.lpush('phobia_kind', 'haptophobia')
self.redis.lpush('phobia_kind', 'harpaxophobia')
self.redis.lpush('phobia_kind', 'hedonophobia')
self.redis.lpush('phobia_kind', 'heliophobia')
self.redis.lpush('phobia_kind', 'hellenologophobia')
self.redis.lpush('phobia_kind', 'helminthophobia')
self.redis.lpush('phobia_kind', 'heresyphobia')
self.redis.lpush('phobia_kind', 'herpetophobia')
self.redis.lpush('phobia_kind', 'hierophobia')
self.redis.lpush('phobia_kind', 'hobophobia')
self.redis.lpush('phobia_kind', 'hodophobia')
self.redis.lpush('phobia_kind', 'homilophobia')
self.redis.lpush('phobia_kind', 'hominophobia')
self.redis.lpush('phobia_kind', 'hormephobia')
self.redis.lpush('phobia_kind', 'hydrargyophobia')
self.redis.lpush('phobia_kind', 'hygrophobia')
self.redis.lpush('phobia_kind', 'hylephobia')
self.redis.lpush('phobia_kind', 'hylophobia')
self.redis.lpush('phobia_kind', 'hypengyophobia')
self.redis.lpush('phobia_kind', 'hypnophobia')
self.redis.lpush('phobia_kind', 'iatrophobia')
self.redis.lpush('phobia_kind', 'ichthyophobia')
self.redis.lpush('phobia_kind', 'ideophobia')
self.redis.lpush('phobia_kind', 'illyngophobia')
self.redis.lpush('phobia_kind', 'isopterophobia')
self.redis.lpush('phobia_kind', 'kakorrhaphiophobia')
self.redis.lpush('phobia_kind', 'katagelophobia')
self.redis.lpush('phobia_kind', 'kathisophobia')
self.redis.lpush('phobia_kind', 'katsaridaphobia')
self.redis.lpush('phobia_kind', 'kinetophobia')
self.redis.lpush('phobia_kind', 'kleptophobia')
self.redis.lpush('phobia_kind', 'koinoniphobia')
self.redis.lpush('phobia_kind', 'koniophobia')
self.redis.lpush('phobia_kind', 'kopophobia')
self.redis.lpush('phobia_kind', 'kosmikophobia')
self.redis.lpush('phobia_kind', 'kymophobia')
self.redis.lpush('phobia_kind', 'kynophobia')
self.redis.lpush('phobia_kind', 'kyphophobia')
self.redis.lpush('phobia_kind', 'lachanophobia')
self.redis.lpush('phobia_kind', 'lalophobia')
self.redis.lpush('phobia_kind', 'leprophobia')
self.redis.lpush('phobia_kind', 'leukophobia')
self.redis.lpush('phobia_kind', 'levophobia')
self.redis.lpush('phobia_kind', 'ligyrophobia')
self.redis.lpush('phobia_kind', 'lilapsophobia')
self.redis.lpush('phobia_kind', 'limnophobia')
self.redis.lpush('phobia_kind', 'linonophobia')
self.redis.lpush('phobia_kind', 'liticaphobia')
self.redis.lpush('phobia_kind', 'logophobia')
self.redis.lpush('phobia_kind', 'luiphobia')
self.redis.lpush('phobia_kind', 'lunaphobia')
self.redis.lpush('phobia_kind', 'lutraphobia')
self.redis.lpush('phobia_kind', 'lygophobia')
self.redis.lpush('phobia_kind', 'lyssophobia')
self.redis.lpush('phobia_kind', 'macrophobia')
self.redis.lpush('phobia_kind', 'mageirocophobia')
self.redis.lpush('phobia_kind', 'mechanophobia')
self.redis.lpush('phobia_kind', 'megalophobia')
self.redis.lpush('phobia_kind', 'melanophobia')
self.redis.lpush('phobia_kind', 'melophobia')
self.redis.lpush('phobia_kind', 'meningitophobia')
self.redis.lpush('phobia_kind', 'merinthophobia')
self.redis.lpush('phobia_kind', 'metallophobia')
self.redis.lpush('phobia_kind', 'metathesiophobia')
self.redis.lpush('phobia_kind', 'meteorophobia')
self.redis.lpush('phobia_kind', 'methyphobia')
self.redis.lpush('phobia_kind', 'metrophobia')
self.redis.lpush('phobia_kind', 'microbiophobia')
self.redis.lpush('phobia_kind', 'microphobia')
self.redis.lpush('phobia_kind', 'mnemophobia')
self.redis.lpush('phobia_kind', 'molysomophobia')
self.redis.lpush('phobia_kind', 'monopathophobia')
self.redis.lpush('phobia_kind', 'monophobia')
self.redis.lpush('phobia_kind', 'mottephobia')
self.redis.lpush('phobia_kind', 'musophobia')
self.redis.lpush('phobia_kind', 'mycophobia')
self.redis.lpush('phobia_kind', 'myrmecophobia')
self.redis.lpush('phobia_kind', 'mythophobia')
self.redis.lpush('phobia_kind', 'myxophobia')
self.redis.lpush('phobia_kind', 'nebulaphobia')
self.redis.lpush('phobia_kind', 'necrophobia')
self.redis.lpush('phobia_kind', 'nelophobia')
self.redis.lpush('phobia_kind', 'neophobia')
self.redis.lpush('phobia_kind', 'nephophobia')
self.redis.lpush('phobia_kind', 'noctiphobia')
self.redis.lpush('phobia_kind', 'nomatophobia')
self.redis.lpush('phobia_kind', 'nosemaphobia')
self.redis.lpush('phobia_kind', 'nosocomephobia')
self.redis.lpush('phobia_kind', 'nostophobia')
self.redis.lpush('phobia_kind', 'novercaphobia')
self.redis.lpush('phobia_kind', 'nucleomituphobia')
self.redis.lpush('phobia_kind', 'nyctohylophobia')
self.redis.lpush('phobia_kind', 'nyctophobia')
self.redis.lpush('phobia_kind', 'ochlophobia')
self.redis.lpush('phobia_kind', 'ochophobia')
self.redis.lpush('phobia_kind', 'octophobia')
self.redis.lpush('phobia_kind', 'odontophobia')
self.redis.lpush('phobia_kind', 'odynephobia')
self.redis.lpush('phobia_kind', 'oenophobia')
self.redis.lpush('phobia_kind', 'oikophobia')
self.redis.lpush('phobia_kind', 'olfactophobia')
self.redis.lpush('phobia_kind', 'ommetaphobia')
self.redis.lpush('phobia_kind', 'omphalophobia')
self.redis.lpush('phobia_kind', 'oneirophobia')
self.redis.lpush('phobia_kind', 'onomatophobia')
self.redis.lpush('phobia_kind', 'ophidiophobia')
self.redis.lpush('phobia_kind', 'ophthalmophobia')
self.redis.lpush('phobia_kind', 'optophobia')
self.redis.lpush('phobia_kind', 'ornithophobia')
self.redis.lpush('phobia_kind', 'orthophobia')
self.redis.lpush('phobia_kind', 'ostraconophobia')
self.redis.lpush('phobia_kind', 'ouranophobia')
self.redis.lpush('phobia_kind', 'pagophobia')
self.redis.lpush('phobia_kind', 'panophobia')
self.redis.lpush('phobia_kind', 'panthophobia')
self.redis.lpush('phobia_kind', 'pantophobia')
self.redis.lpush('phobia_kind', 'papyrophobia')
self.redis.lpush('phobia_kind', 'paralipophobia')
self.redis.lpush('phobia_kind', 'parasitophobia')
self.redis.lpush('phobia_kind', 'parthenophobia')
self.redis.lpush('phobia_kind', 'pathophobia')
self.redis.lpush('phobia_kind', 'patroiophobia')
self.redis.lpush('phobia_kind', 'peccatophobia')
self.redis.lpush('phobia_kind', 'pediophobia')
self.redis.lpush('phobia_kind', 'pedophobia')
self.redis.lpush('phobia_kind', 'peladophobia')
self.redis.lpush('phobia_kind', 'pellagrophobia')
self.redis.lpush('phobia_kind', 'peniaphobia')
self.redis.lpush('phobia_kind', 'pentheraphobia')
self.redis.lpush('phobia_kind', 'phagophobia')
self.redis.lpush('phobia_kind', 'phalacrophobia')
self.redis.lpush('phobia_kind', 'pharmacophobia')
self.redis.lpush('phobia_kind', 'pharmcophobia')
self.redis.lpush('phobia_kind', 'phasmophobia')
self.redis.lpush('phobia_kind', 'phengophobia')
self.redis.lpush('phobia_kind', 'phenogophobia')
self.redis.lpush('phobia_kind', 'philematophobia')
self.redis.lpush('phobia_kind', 'philophobia')
self.redis.lpush('phobia_kind', 'philosophobia')
self.redis.lpush('phobia_kind', 'phobophobia')
self.redis.lpush('phobia_kind', 'phonophobia')
self.redis.lpush('phobia_kind', 'photalgiophobia')
self.redis.lpush('phobia_kind', 'photoaugliaphobia')
self.redis.lpush('phobia_kind', 'photophobia')
self.redis.lpush('phobia_kind', 'phronemophobia')
self.redis.lpush('phobia_kind', 'phthiriophobia')
self.redis.lpush('phobia_kind', 'phthisiophobia')
self.redis.lpush('phobia_kind', 'placophobia')
self.redis.lpush('phobia_kind', 'plutophobia')
self.redis.lpush('phobia_kind', 'pluviophobia')
self.redis.lpush('phobia_kind', 'pneumatophobia')
self.redis.lpush('phobia_kind', 'pnigophobia')
self.redis.lpush('phobia_kind', 'pocrescophobia')
self.redis.lpush('phobia_kind', 'pogonophobia')
self.redis.lpush('phobia_kind', 'poinephobia')
self.redis.lpush('phobia_kind', 'poliosophobia')
self.redis.lpush('phobia_kind', 'politicophobia')
self.redis.lpush('phobia_kind', 'polyphobia')
self.redis.lpush('phobia_kind', 'ponophobia')
self.redis.lpush('phobia_kind', 'porphyrophobia')
self.redis.lpush('phobia_kind', 'potamophobia')
self.redis.lpush('phobia_kind', 'prosophobia')
self.redis.lpush('phobia_kind', 'psellismophobia')
self.redis.lpush('phobia_kind', 'psychophobia')
self.redis.lpush('phobia_kind', 'pteronophobia')
self.redis.lpush('phobia_kind', 'pupaphobia')
self.redis.lpush('phobia_kind', 'pyrexiophobia')
self.redis.lpush('phobia_kind', 'pyrophobia')
self.redis.lpush('phobia_kind', 'radiophobia')
self.redis.lpush('phobia_kind', 'ranidaphobia')
self.redis.lpush('phobia_kind', 'rhabdophobia')
self.redis.lpush('phobia_kind', 'rhytiphobia')
self.redis.lpush('phobia_kind', 'rupophobia')
self.redis.lpush('phobia_kind', 'scabiophobia')
self.redis.lpush('phobia_kind', 'scelerophobia')
self.redis.lpush('phobia_kind', 'scholionophobia')
self.redis.lpush('phobia_kind', 'sciophobia')
self.redis.lpush('phobia_kind', 'scoleciphobia')
self.redis.lpush('phobia_kind', 'scoptophobia')
self.redis.lpush('phobia_kind', 'scotomaphobia')
self.redis.lpush('phobia_kind', 'scriptophobia')
self.redis.lpush('phobia_kind', 'selachophobia')
self.redis.lpush('phobia_kind', 'selaphobia')
self.redis.lpush('phobia_kind', 'selenophobia')
self.redis.lpush('phobia_kind', 'septophobia')
self.redis.lpush('phobia_kind', 'sesquipedalophobia')
self.redis.lpush('phobia_kind', 'siderophobia')
self.redis.lpush('phobia_kind', 'sinistrophobia')
self.redis.lpush('phobia_kind', 'soceraphobia')
self.redis.lpush('phobia_kind', 'sociophobia')
self.redis.lpush('phobia_kind', 'somniphobia')
self.redis.lpush('phobia_kind', 'sophophobia')
self.redis.lpush('phobia_kind', 'soteriophobia')
self.redis.lpush('phobia_kind', 'spacephobia')
self.redis.lpush('phobia_kind', 'spectrophobia')
self.redis.lpush('phobia_kind', 'spheksophobia')
self.redis.lpush('phobia_kind', 'stasiphobia')
self.redis.lpush('phobia_kind', 'stenophobia')
self.redis.lpush('phobia_kind', 'stygiophobia')
self.redis.lpush('phobia_kind', 'symbolophobia')
self.redis.lpush('phobia_kind', 'symmetrophobia')
self.redis.lpush('phobia_kind', 'syngenesophobia')
self.redis.lpush('phobia_kind', 'syphilophobia')
self.redis.lpush('phobia_kind', 'tabophobia')
self.redis.lpush('phobia_kind', 'tachophobia')
self.redis.lpush('phobia_kind', 'taphophobia')
self.redis.lpush('phobia_kind', 'tapinophobia')
self.redis.lpush('phobia_kind', 'taurophobia')
self.redis.lpush('phobia_kind', 'technophobia')
self.redis.lpush('phobia_kind', 'teleophobia')
self.redis.lpush('phobia_kind', 'teniophobia')
self.redis.lpush('phobia_kind', 'teratophobia')
self.redis.lpush('phobia_kind', 'testophobia')
self.redis.lpush('phobia_kind', 'tetanophobia')
self.redis.lpush('phobia_kind', 'textophobia')
self.redis.lpush('phobia_kind', 'thaasophobia')
self.redis.lpush('phobia_kind', 'thalassophobia')
self.redis.lpush('phobia_kind', 'thanatophobia')
self.redis.lpush('phobia_kind', 'theatrophobia')
self.redis.lpush('phobia_kind', 'theologicophobia')
self.redis.lpush('phobia_kind', 'theophobia')
self.redis.lpush('phobia_kind', 'thermophobia')
self.redis.lpush('phobia_kind', 'thixophobia')
self.redis.lpush('phobia_kind', 'tokophobia')
self.redis.lpush('phobia_kind', 'tomophobia')
self.redis.lpush('phobia_kind', 'topophobia')
self.redis.lpush('phobia_kind', 'toxiphobia')
self.redis.lpush('phobia_kind', 'traumatophobia')
self.redis.lpush('phobia_kind', 'tremophobia')
self.redis.lpush('phobia_kind', 'trichopathophobia')
self.redis.lpush('phobia_kind', 'trichophobia')
self.redis.lpush('phobia_kind', 'triskaidekaphobia')
self.redis.lpush('phobia_kind', 'tropophobia')
self.redis.lpush('phobia_kind', 'trypanophobia')
self.redis.lpush('phobia_kind', 'tyrannophobia')
self.redis.lpush('phobia_kind', 'vaccinophobia')
self.redis.lpush('phobia_kind', 'venustraphobia')
self.redis.lpush('phobia_kind', 'verminophobia')
self.redis.lpush('phobia_kind', 'vermiphobia')
self.redis.lpush('phobia_kind', 'vestiphobia')
self.redis.lpush('phobia_kind', 'vitricophobia')
self.redis.lpush('phobia_kind', 'wiccaphobia')
self.redis.lpush('phobia_kind', 'xanthophobia')
self.redis.lpush('phobia_kind', 'xenoglossophobia')
self.redis.lpush('phobia_kind', 'xenophobia')
self.redis.lpush('phobia_kind', 'xerophobia')
self.redis.lpush('phobia_kind', 'xylophobia')
self.redis.lpush('phobia_kind', 'xyrophobia')
self.redis.lpush('phobia_kind', 'zelophobia')
self.redis.lpush('phobia_kind', 'zeusophobia')
self.redis.lpush('phobia_kind', 'zoophobia')







HSET phobia_kind_description ablutophobia       {"name":"Ablutophobia",       "description":"washing or bathing" }
HSET phobia_kind_description acarophobia        {"name":"Acarophobia",        "description":"skin infestation by mites or ticks" }
HSET phobia_kind_description acerophobia        {"name":"Acerophobia",        "description":"sourness" }
HSET phobia_kind_description acousticophobia    {"name":"Acousticophobia",    "description":"noise" }
HSET phobia_kind_description acrophobia         {"name":"Acrophobia",         "description":"heights" }
HSET phobia_kind_description aeroacrophobia     {"name":"Aeroacrophobia",     "description":"open high places" }
HSET phobia_kind_description aeronausiphobia    {"name":"Aeronausiphobia",    "description":"vomiting due to airsickness" }
HSET phobia_kind_description aerophobia         {"name":"Aerophobia",         "description":"drafts, air swallowing, or airbourne noxious substances" }
HSET phobia_kind_description agoraphobia        {"name":"Agoraphobia",        "description":"open spaces or of being in crowded, public places" }
HSET phobia_kind_description agrizoophobia      {"name":"Agrizoophobia",      "description":"wild animals" }
HSET phobia_kind_description agyrophobia        {"name":"Agyrophobia",        "description":"crossing streets" }
HSET phobia_kind_description aibohphobia        {"name":"Aibohphobia",        "description":"palindromes" }
HSET phobia_kind_description aichmophobia       {"name":"Aichmophobia",       "description":"sharp things, like pins and needles" }
HSET phobia_kind_description albuminurophobia   {"name":"Albuminurophobia",   "description":"kidney disease" }
HSET phobia_kind_description alektorophobia     {"name":"Alektorophobia",     "description":"chickens" }
HSET phobia_kind_description alliumphobia       {"name":"Alliumphobia",       "description":"garlic" }
HSET phobia_kind_description allodoxaphobia     {"name":"Allodoxaphobia",     "description":"opinions" }
HSET phobia_kind_description altophobia         {"name":"Altophobia",         "description":"high places" }
HSET phobia_kind_description amaxophobia        {"name":"Amaxophobia",        "description":"being in or riding in vehicles" }
HSET phobia_kind_description ambulophobia       {"name":"Ambulophobia",       "description":"walking" }
HSET phobia_kind_description amnesiphobia       {"name":"Amnesiphobia",       "description":"amnesia" }
HSET phobia_kind_description amychophobia       {"name":"Amychophobia",       "description":"scratches or being scratched" }
HSET phobia_kind_description anablephobia       {"name":"Anablephobia",       "description":"looking up" }
HSET phobia_kind_description ancraophobia       {"name":"Ancraophobia",       "description":"wind or drafts" }
HSET phobia_kind_description androphobia        {"name":"Androphobia",        "description":"men" }
HSET phobia_kind_description anemophobia        {"name":"Anemophobia",        "description":"drafts of wind" }
HSET phobia_kind_description anginophobia       {"name":"Anginophobia",       "description":"choking or smothering" }
HSET phobia_kind_description angrophobia        {"name":"Angrophobia",        "description":"anger or of becoming angry" }
HSET phobia_kind_description ankylophobia       {"name":"Ankylophobia",       "description":"immobility of a joint" }
HSET phobia_kind_description anthrophobia       {"name":"Anthrophobia",       "description":"flowers" }
HSET phobia_kind_description anthropophobia     {"name":"Anthropophobia",     "description":"people or company" }
HSET phobia_kind_description antlophobia        {"name":"Antlophobia",        "description":"floods" }
HSET phobia_kind_description anuptaphobia       {"name":"Anuptaphobia",       "description":"staying single" }
HSET phobia_kind_description apeirophobia       {"name":"Apeirophobia",       "description":"infinity" }
HSET phobia_kind_description aphephobia         {"name":"Aphephobia",         "description":"touching or being touched" }
HSET phobia_kind_description apiphobia          {"name":"Apiphobia",          "description":"bees" }
HSET phobia_kind_description apotemnophobia     {"name":"Apotemnophobia",     "description":"persons with amputations" }
HSET phobia_kind_description aquaphobia         {"name":"Aquaphobia",         "description":"water" }
HSET phobia_kind_description arachibutyrophobia {"name":"Arachibutyrophobia", "description":"peanut butter sticking to the roof of the mouth" }
HSET phobia_kind_description arachnophobia      {"name":"Arachnophobia",      "description":"spiders" }
HSET phobia_kind_description arithmophobia      {"name":"Arithmophobia",      "description":"numbers" }
HSET phobia_kind_description arsonphobia        {"name":"Arsonphobia",        "description":"causing a fire" }
HSET phobia_kind_description asthenophobia      {"name":"Asthenophobia",      "description":"fainting or weakness" }
HSET phobia_kind_description astraphobia        {"name":"Astraphobia",        "description":"lightning" }
HSET phobia_kind_description astrapophobia      {"name":"Astrapophobia",      "description":"thunder and lightning" }
HSET phobia_kind_description astrophobia        {"name":"Astrophobia",        "description":"stars or celestial space" }
HSET phobia_kind_description asymmetriphobia    {"name":"Asymmetriphobia",    "description":"asymmetrical things" }
HSET phobia_kind_description ataxiophobia       {"name":"Ataxiophobia",       "description":"muscular incoordination" }
HSET phobia_kind_description ataxophobia        {"name":"Ataxophobia",        "description":"disorder or untidiness" }
HSET phobia_kind_description atelophobia        {"name":"Atelophobia",        "description":"imperfection" }
HSET phobia_kind_description atephobia          {"name":"Atephobia",          "description":"ruins" }
HSET phobia_kind_description athazagoraphobia   {"name":"Athazagoraphobia",   "description":"being forgotten or ignored or forgetting" }
HSET phobia_kind_description atychiphobia       {"name":"Atychiphobia",       "description":"failure" }
HSET phobia_kind_description aulophobia         {"name":"Aulophobia",         "description":"flutes" }
HSET phobia_kind_description aurophobia         {"name":"Aurophobia",         "description":"gold" }
HSET phobia_kind_description auroraphobia       {"name":"Auroraphobia",       "description":"northern lights" }
HSET phobia_kind_description autodysomophobia   {"name":"Autodysomophobia",   "description":"one that has a vile odor" }
HSET phobia_kind_description automatonophobia   {"name":"Automatonophobia",   "description":"anything that falsly represents a sentient being" }
HSET phobia_kind_description automysophobia     {"name":"Automysophobia",     "description":"being dirty" }
HSET phobia_kind_description autophobia         {"name":"Autophobia",         "description":"being alone" }
HSET phobia_kind_description aviophobia         {"name":"Aviophobia",         "description":"flying" }
HSET phobia_kind_description bacillophobia      {"name":"Bacillophobia",      "description":"bacteria" }
HSET phobia_kind_description ballistophobia     {"name":"Ballistophobia",     "description":"missiles or projectiles" }
HSET phobia_kind_description barophobia         {"name":"Barophobia",         "description":"gravity" }
HSET phobia_kind_description basiphobia         {"name":"Basiphobia",         "description":"inability to stand or walk" }
HSET phobia_kind_description bathmophobia       {"name":"Bathmophobia",       "description":"stairs or steep slopes" }
HSET phobia_kind_description bathophobia        {"name":"Bathophobia",        "description":"depth" }
HSET phobia_kind_description batophobia         {"name":"Batophobia",         "description":"heights or being close to high buildings" }
HSET phobia_kind_description batrachophobia     {"name":"Batrachophobia",     "description":"amphibians, such as frogs, newts, salamanders, etc" }
HSET phobia_kind_description belomophobia       {"name":"Belomophobia",       "description":"needles" }
HSET phobia_kind_description bibliophobia       {"name":"Bibliophobia",       "description":"books" }
HSET phobia_kind_description bogyphobia         {"name":"Bogyphobia",         "description":"the bogeyman" }
HSET phobia_kind_description botanophobia       {"name":"Botanophobia",       "description":"plants" }
HSET phobia_kind_description bromidrophobia     {"name":"Bromidrophobia",     "description":"body smells" }
HSET phobia_kind_description brontophobia       {"name":"Brontophobia",       "description":"thunder storms" }
HSET phobia_kind_description bufonophobia       {"name":"Bufonophobia",       "description":"toads" }
HSET phobia_kind_description cacomorphobia      {"name":"Cacomorphobia",      "description":"fat people" }
HSET phobia_kind_description cacophobia         {"name":"Cacophobia",         "description":"ugliness" }
HSET phobia_kind_description cainophobia        {"name":"Cainophobia",        "description":"novelty" }
HSET phobia_kind_description cainotophobia      {"name":"Cainotophobia",      "description":"newness" }
HSET phobia_kind_description carcinophobia      {"name":"Carcinophobia",      "description":"cancer" }
HSET phobia_kind_description cardiophobia       {"name":"Cardiophobia",       "description":"the heart or heart disease" }
HSET phobia_kind_description carnophobia        {"name":"Carnophobia",        "description":"meat" }
HSET phobia_kind_description catagelophobia     {"name":"Catagelophobia",     "description":"being ridiculed" }
HSET phobia_kind_description catapedaphobia     {"name":"Catapedaphobia",     "description":"jumping from high and low places" }
HSET phobia_kind_description cathisophobia      {"name":"Cathisophobia",      "description":"sitting" }
HSET phobia_kind_description catoptrophobia     {"name":"Catoptrophobia",     "description":"mirrors" }
HSET phobia_kind_description cenophobia         {"name":"Cenophobia",         "description":"empty spaces" }
HSET phobia_kind_description centophobia        {"name":"Centophobia",        "description":"new ideas" }
HSET phobia_kind_description ceraunophobia      {"name":"Ceraunophobia",      "description":"thunder" }
HSET phobia_kind_description chemophobia        {"name":"Chemophobia",        "description":"chemicals or working with chemicals" }
HSET phobia_kind_description cherophobia        {"name":"Cherophobia",        "description":"gaiety" }
HSET phobia_kind_description chinophobia        {"name":"Chinophobia",        "description":"snow" }
HSET phobia_kind_description chiraptophobia     {"name":"Chiraptophobia",     "description":"being touched" }
HSET phobia_kind_description chirophobia        {"name":"Chirophobia",        "description":"hands" }
HSET phobia_kind_description chiroptophobia     {"name":"Chiroptophobia",     "description":"bats" }
HSET phobia_kind_description cholerophobia      {"name":"Cholerophobia",      "description":"cholera" }
HSET phobia_kind_description chorophobia        {"name":"Chorophobia",        "description":"dancing" }
HSET phobia_kind_description chrometophobia     {"name":"Chrometophobia",     "description":"money" }
HSET phobia_kind_description chromophobia       {"name":"Chromophobia",       "description":"colors" }
HSET phobia_kind_description chronomentrophobia {"name":"Chronomentrophobia", "description":"clocks" }
HSET phobia_kind_description chronophobia       {"name":"Chronophobia",       "description":"time" }
HSET phobia_kind_description cibophobia         {"name":"Cibophobia",         "description":"food" }
HSET phobia_kind_description claustrophobia     {"name":"Claustrophobia",     "description":"confined spaces" }
HSET phobia_kind_description cleithrophobia     {"name":"Cleithrophobia",     "description":"being enclosed" }
HSET phobia_kind_description climacophobia      {"name":"Climacophobia",      "description":"stairs, climbing, or of falling downstairs" }
HSET phobia_kind_description clinophobia        {"name":"Clinophobia",        "description":"beds" }
HSET phobia_kind_description cnidophobia        {"name":"Cnidophobia",        "description":"insect stings" }
HSET phobia_kind_description coimetrophobia     {"name":"Coimetrophobia",     "description":"cemeteries" }
HSET phobia_kind_description cometophobia       {"name":"Cometophobia",       "description":"comets" }
HSET phobia_kind_description consecotaleophobia {"name":"Consecotaleophobia", "description":"chopsticks" }
HSET phobia_kind_description coprastasophobia   {"name":"Coprastasophobia",   "description":"constipation" }
HSET phobia_kind_description coulrophobia       {"name":"Coulrophobia",       "description":"clowns" }
HSET phobia_kind_description cremnophobia       {"name":"Cremnophobia",       "description":"precipices" }
HSET phobia_kind_description cryophobia         {"name":"Cryophobia",         "description":"extreme cold, ice or frost" }
HSET phobia_kind_description crystallophobia    {"name":"Crystallophobia",    "description":"crystals or glass" }
HSET phobia_kind_description cyclophobia        {"name":"Cyclophobia",        "description":"bicycles" }
HSET phobia_kind_description cynophobia         {"name":"Cynophobia",         "description":"dogs" }
HSET phobia_kind_description daemonophobia      {"name":"Daemonophobia",      "description":"demons" }
HSET phobia_kind_description decidophobia       {"name":"Decidophobia",       "description":"making decisions" }
HSET phobia_kind_description deipnophobia       {"name":"Deipnophobia",       "description":"dining or dinner conversations" }
HSET phobia_kind_description dementophobia      {"name":"Dementophobia",      "description":"insanity" }
HSET phobia_kind_description demonophobia       {"name":"Demonophobia",       "description":"spirits or demons" }
HSET phobia_kind_description demophobia         {"name":"Demophobia",         "description":"crowds" }
HSET phobia_kind_description dendrophobia       {"name":"Dendrophobia",       "description":"trees" }
HSET phobia_kind_description dermatopathophobia {"name":"Dermatopathophobia", "description":"skin disease" }
HSET phobia_kind_description dermatophobia      {"name":"Dermatophobia",      "description":"skin" }
HSET phobia_kind_description dextrophobia       {"name":"Dextrophobia",       "description":"objects on the right side of the body" }
HSET phobia_kind_description diabetophobia      {"name":"Diabetophobia",      "description":"diabetes" }
HSET phobia_kind_description didaskaleinophobia {"name":"Didaskaleinophobia", "description":"going to school" }
HSET phobia_kind_description dikephobia         {"name":"Dikephobia",         "description":"justice" }
HSET phobia_kind_description dinophobia         {"name":"Dinophobia",         "description":"dizziness or whirlpools" }
HSET phobia_kind_description diplophobia        {"name":"Diplophobia",        "description":"double vision" }
HSET phobia_kind_description dipsophobia        {"name":"Dipsophobia",        "description":"drinking" }
HSET phobia_kind_description dishabiliophobia   {"name":"Dishabiliophobia",   "description":"undressing in front of someone" }
HSET phobia_kind_description disposophobia      {"name":"Disposophobia",      "description":"throwing stuff out" }
HSET phobia_kind_description domatophobia       {"name":"Domatophobia",       "description":"being in a house" }
HSET phobia_kind_description doraphobia         {"name":"Doraphobia",         "description":"fur or skins of animals" }
HSET phobia_kind_description doxophobia         {"name":"Doxophobia",         "description":"expressing opinions or of receiving praise" }
HSET phobia_kind_description dysmorphophobia    {"name":"Dysmorphophobia",    "description":"deformity" }
HSET phobia_kind_description dystychiphobia     {"name":"Dystychiphobia",     "description":"accidents" }
HSET phobia_kind_description ecclesiophobia     {"name":"Ecclesiophobia",     "description":"church" }
HSET phobia_kind_description ecophobia          {"name":"Ecophobia",          "description":"home" }
HSET phobia_kind_description eisoptrophobia     {"name":"Eisoptrophobia",     "description":"looking into mirrors" }
HSET phobia_kind_description electrophobia      {"name":"Electrophobia",      "description":"electricity" }
HSET phobia_kind_description eleutherophobia    {"name":"Eleutherophobia",    "description":"freedom" }
HSET phobia_kind_description emetophobia        {"name":"Emetophobia",        "description":"vomiting" }
HSET phobia_kind_description enetophobia        {"name":"Enetophobia",        "description":"pins" }
HSET phobia_kind_description enosiophobia       {"name":"Enosiophobia",       "description":"having committed an unpardonable sin" }
HSET phobia_kind_description entomophobia       {"name":"Entomophobia",       "description":"insects" }
HSET phobia_kind_description eosophobia         {"name":"Eosophobia",         "description":"dawn or daylight" }
HSET phobia_kind_description ephebiphobia       {"name":"Ephebiphobia",       "description":"teenagers" }
HSET phobia_kind_description epistaxiophobia    {"name":"Epistaxiophobia",    "description":"nosebleeds" }
HSET phobia_kind_description epistemophobia     {"name":"Epistemophobia",     "description":"knowledge" }
HSET phobia_kind_description equinophobia       {"name":"Equinophobia",       "description":"horses" }
HSET phobia_kind_description eremophobia        {"name":"Eremophobia",        "description":"being alone" }
HSET phobia_kind_description ereuthophobia      {"name":"Ereuthophobia",      "description":"red" }
HSET phobia_kind_description ereuthrophobia     {"name":"Ereuthrophobia",     "description":"blushing" }
HSET phobia_kind_description ergasiophobia      {"name":"Ergasiophobia",      "description":"work or functioning" }
HSET phobia_kind_description ergophobia         {"name":"Ergophobia",         "description":"work" }
HSET phobia_kind_description erythrophobia      {"name":"Erythrophobia",      "description":"redlights" }
HSET phobia_kind_description euphobia           {"name":"Euphobia",           "description":"hearing good news" }
HSET phobia_kind_description felinophobia       {"name":"Felinophobia",       "description":"cats" }
HSET phobia_kind_description frigophobia        {"name":"Frigophobia",        "description":"cold or cold things" }
HSET phobia_kind_description gametophobia       {"name":"Gametophobia",       "description":"marriage" }
HSET phobia_kind_description geliophobia        {"name":"Geliophobia",        "description":"laughter" }
HSET phobia_kind_description gelotophobia       {"name":"Gelotophobia",       "description":"being laughed at" }
HSET phobia_kind_description geniophobia        {"name":"Geniophobia",        "description":"chins" }
HSET phobia_kind_description genuphobia         {"name":"Genuphobia",         "description":"knees" }
HSET phobia_kind_description gephyrophobia      {"name":"Gephyrophobia",      "description":"crossing bridges" }
HSET phobia_kind_description gerascophobia      {"name":"Gerascophobia",      "description":"growing old" }
HSET phobia_kind_description gerontophobia      {"name":"Gerontophobia",      "description":"old people or of growing old" }
HSET phobia_kind_description geumophobia        {"name":"Geumophobia",        "description":"taste" }
HSET phobia_kind_description glossophobia       {"name":"Glossophobia",       "description":"speaking in public or of trying to speak" }
HSET phobia_kind_description graphophobia       {"name":"Graphophobia",       "description":"writing" }
HSET phobia_kind_description gynophobia         {"name":"Gynophobia",         "description":"women" }
HSET phobia_kind_description haemaphobia        {"name":"Haemaphobia",        "description":"blood" }
HSET phobia_kind_description haematophobia      {"name":"Haematophobia",      "description":"blood diseases" }
HSET phobia_kind_description hagiophobia        {"name":"Hagiophobia",        "description":"saints" }
HSET phobia_kind_description hamartophobia      {"name":"Hamartophobia",      "description":"sinning" }
HSET phobia_kind_description haptophobia        {"name":"Haptophobia",        "description":"touch" }
HSET phobia_kind_description harpaxophobia      {"name":"Harpaxophobia",      "description":"being robbed" }
HSET phobia_kind_description hedonophobia       {"name":"Hedonophobia",       "description":"feeling pleasure" }
HSET phobia_kind_description heliophobia        {"name":"Heliophobia",        "description":"the sun" }
HSET phobia_kind_description hellenologophobia  {"name":"Hellenologophobia",  "description":"complex scientific terminology" }
HSET phobia_kind_description helminthophobia    {"name":"Helminthophobia",    "description":"being infested with worms" }
HSET phobia_kind_description heresyphobia       {"name":"Heresyphobia",       "description":"challenges to official doctrine or of radical deviation" }
HSET phobia_kind_description herpetophobia      {"name":"Herpetophobia",      "description":"reptiles" }
HSET phobia_kind_description hierophobia        {"name":"Hierophobia",        "description":"sacred objects" }
HSET phobia_kind_description hobophobia         {"name":"Hobophobia",         "description":"bums or beggars" }
HSET phobia_kind_description hodophobia         {"name":"Hodophobia",         "description":"road travel" }
HSET phobia_kind_description homilophobia       {"name":"Homilophobia",       "description":"sermons" }
HSET phobia_kind_description hominophobia       {"name":"Hominophobia",       "description":"humans" }
HSET phobia_kind_description hormephobia        {"name":"Hormephobia",        "description":"shock" }
HSET phobia_kind_description hydrargyophobia    {"name":"Hydrargyophobia",    "description":"mercurial medicines" }
HSET phobia_kind_description hygrophobia        {"name":"Hygrophobia",        "description":"liquids, dampness, or moisture" }
HSET phobia_kind_description hylephobia         {"name":"Hylephobia",         "description":"wood or woods" }
HSET phobia_kind_description hylophobia         {"name":"Hylophobia",         "description":"forests" }
HSET phobia_kind_description hypengyophobia     {"name":"Hypengyophobia",     "description":"responsibility" }
HSET phobia_kind_description hypnophobia        {"name":"Hypnophobia",        "description":"sleep or of being hypnotized" }
HSET phobia_kind_description iatrophobia        {"name":"Iatrophobia",        "description":"going to the doctor" }
HSET phobia_kind_description ichthyophobia      {"name":"Ichthyophobia",      "description":"fish" }
HSET phobia_kind_description ideophobia         {"name":"Ideophobia",         "description":"ideas" }
HSET phobia_kind_description illyngophobia      {"name":"Illyngophobia",      "description":"vertigo or feeling dizzy when looking down" }
HSET phobia_kind_description isopterophobia     {"name":"Isopterophobia",     "description":"termites" }
HSET phobia_kind_description kakorrhaphiophobia {"name":"Kakorrhaphiophobia", "description":"failure or defeat" }
HSET phobia_kind_description katagelophobia     {"name":"Katagelophobia",     "description":"ridicule" }
HSET phobia_kind_description kathisophobia      {"name":"Kathisophobia",      "description":"sitting down" }
HSET phobia_kind_description katsaridaphobia    {"name":"Katsaridaphobia",    "description":"cockroaches" }
HSET phobia_kind_description kinetophobia       {"name":"Kinetophobia",       "description":"movement or motion" }
HSET phobia_kind_description kleptophobia       {"name":"Kleptophobia",       "description":"theft and thieves" }
HSET phobia_kind_description koinoniphobia      {"name":"Koinoniphobia",      "description":"rooms" }
HSET phobia_kind_description koniophobia        {"name":"Koniophobia",        "description":"dust" }
HSET phobia_kind_description kopophobia         {"name":"Kopophobia",         "description":"fatigue" }
HSET phobia_kind_description kosmikophobia      {"name":"Kosmikophobia",      "description":"cosmic phenomenon" }
HSET phobia_kind_description kymophobia         {"name":"Kymophobia",         "description":"waves or wave like motions" }
HSET phobia_kind_description kynophobia         {"name":"Kynophobia",         "description":"rabies" }
HSET phobia_kind_description kyphophobia        {"name":"Kyphophobia",        "description":"stooping" }
HSET phobia_kind_description lachanophobia      {"name":"Lachanophobia",      "description":"vegetables" }
HSET phobia_kind_description lalophobia         {"name":"Lalophobia",         "description":"speaking" }
HSET phobia_kind_description leprophobia        {"name":"Leprophobia",        "description":"leprosy" }
HSET phobia_kind_description leukophobia        {"name":"Leukophobia",        "description":"the color white" }
HSET phobia_kind_description levophobia         {"name":"Levophobia",         "description":"objects on the left side of the body" }
HSET phobia_kind_description ligyrophobia       {"name":"Ligyrophobia",       "description":"loud noises" }
HSET phobia_kind_description lilapsophobia      {"name":"Lilapsophobia",      "description":"tornadoes" }
HSET phobia_kind_description limnophobia        {"name":"Limnophobia",        "description":"lakes" }
HSET phobia_kind_description linonophobia       {"name":"Linonophobia",       "description":"string" }
HSET phobia_kind_description liticaphobia       {"name":"Liticaphobia",       "description":"lawsuits" }
HSET phobia_kind_description logophobia         {"name":"Logophobia",         "description":"words" }
HSET phobia_kind_description luiphobia          {"name":"Luiphobia",          "description":"lues, syphillis" }
HSET phobia_kind_description lunaphobia         {"name":"Lunaphobia",         "description":"the moon" }
HSET phobia_kind_description lutraphobia        {"name":"Lutraphobia",        "description":"otters" }
HSET phobia_kind_description lygophobia         {"name":"Lygophobia",         "description":"darkness" }
HSET phobia_kind_description lyssophobia        {"name":"Lyssophobia",        "description":"becoming insane" }
HSET phobia_kind_description macrophobia        {"name":"Macrophobia",        "description":"long waits" }
HSET phobia_kind_description mageirocophobia    {"name":"Mageirocophobia",    "description":"cooking" }
HSET phobia_kind_description mechanophobia      {"name":"Mechanophobia",      "description":"machines" }
HSET phobia_kind_description megalophobia       {"name":"Megalophobia",       "description":"large things" }
HSET phobia_kind_description melanophobia       {"name":"Melanophobia",       "description":"the color black" }
HSET phobia_kind_description melophobia         {"name":"Melophobia",         "description":"music" }
HSET phobia_kind_description meningitophobia    {"name":"Meningitophobia",    "description":"brain disease" }
HSET phobia_kind_description merinthophobia     {"name":"Merinthophobia",     "description":"being bound or tied up" }
HSET phobia_kind_description metallophobia      {"name":"Metallophobia",      "description":"metal" }
HSET phobia_kind_description metathesiophobia   {"name":"Metathesiophobia",   "description":"changes" }
HSET phobia_kind_description meteorophobia      {"name":"Meteorophobia",      "description":"meteors or meteorites" }
HSET phobia_kind_description methyphobia        {"name":"Methyphobia",        "description":"alcohol" }
HSET phobia_kind_description metrophobia        {"name":"Metrophobia",        "description":"poetry" }
HSET phobia_kind_description microbiophobia     {"name":"Microbiophobia",     "description":"microbes" }
HSET phobia_kind_description microphobia        {"name":"Microphobia",        "description":"small things" }
HSET phobia_kind_description mnemophobia        {"name":"Mnemophobia",        "description":"memories" }
HSET phobia_kind_description molysomophobia     {"name":"Molysomophobia",     "description":"dirt or contamination" }
HSET phobia_kind_description monopathophobia    {"name":"Monopathophobia",    "description":"specific diseases or sicknesses" }
HSET phobia_kind_description monophobia         {"name":"Monophobia",         "description":"solitude or being alone" }
HSET phobia_kind_description mottephobia        {"name":"Mottephobia",        "description":"moths" }
HSET phobia_kind_description musophobia         {"name":"Musophobia",         "description":"mice" }
HSET phobia_kind_description mycophobia         {"name":"Mycophobia",         "description":"mushrooms" }
HSET phobia_kind_description myrmecophobia      {"name":"Myrmecophobia",      "description":"ants" }
HSET phobia_kind_description mythophobia        {"name":"Mythophobia",        "description":"making false statements, including retelling myths or stories" }
HSET phobia_kind_description myxophobia         {"name":"Myxophobia",         "description":"slime" }
HSET phobia_kind_description nebulaphobia       {"name":"Nebulaphobia",       "description":"fog" }
HSET phobia_kind_description necrophobia        {"name":"Necrophobia",        "description":"death or dead things" }
HSET phobia_kind_description nelophobia         {"name":"Nelophobia",         "description":"glass" }
HSET phobia_kind_description neophobia          {"name":"Neophobia",          "description":"anything new" }
HSET phobia_kind_description nephophobia        {"name":"Nephophobia",        "description":"clouds" }
HSET phobia_kind_description noctiphobia        {"name":"Noctiphobia",        "description":"the night" }
HSET phobia_kind_description nomatophobia       {"name":"Nomatophobia",       "description":"names" }
HSET phobia_kind_description nosemaphobia       {"name":"Nosemaphobia",       "description":"becoming ill" }
HSET phobia_kind_description nosocomephobia     {"name":"Nosocomephobia",     "description":"hospitals" }
HSET phobia_kind_description nostophobia        {"name":"Nostophobia",        "description":"returning home" }
HSET phobia_kind_description novercaphobia      {"name":"Novercaphobia",      "description":"step-mothers" }
HSET phobia_kind_description nucleomituphobia   {"name":"Nucleomituphobia",   "description":"nuclear weapons" }
HSET phobia_kind_description nyctohylophobia    {"name":"Nyctohylophobia",    "description":"dark wooded areas or of forests at night" }
HSET phobia_kind_description nyctophobia        {"name":"Nyctophobia",        "description":"the dark" }
HSET phobia_kind_description ochlophobia        {"name":"Ochlophobia",        "description":"crowds or mobs" }
HSET phobia_kind_description ochophobia         {"name":"Ochophobia",         "description":"vehicles" }
HSET phobia_kind_description octophobia         {"name":"Octophobia",         "description":"the figure 8" }
HSET phobia_kind_description odontophobia       {"name":"Odontophobia",       "description":"teeth" }
HSET phobia_kind_description odynephobia        {"name":"Odynephobia",        "description":"pain" }
HSET phobia_kind_description oenophobia         {"name":"Oenophobia",         "description":"wine" }
HSET phobia_kind_description oikophobia         {"name":"Oikophobia",         "description":"home" }
HSET phobia_kind_description olfactophobia      {"name":"Olfactophobia",      "description":"smells" }
HSET phobia_kind_description ommetaphobia       {"name":"Ommetaphobia",       "description":"eyes" }
HSET phobia_kind_description omphalophobia      {"name":"Omphalophobia",      "description":"belly buttons" }
HSET phobia_kind_description oneirophobia       {"name":"Oneirophobia",       "description":"dreams" }
HSET phobia_kind_description onomatophobia      {"name":"Onomatophobia",      "description":"hearing a certain word or of names" }
HSET phobia_kind_description ophidiophobia      {"name":"Ophidiophobia",      "description":"snakes" }
HSET phobia_kind_description ophthalmophobia    {"name":"Ophthalmophobia",    "description":"being stared at" }
HSET phobia_kind_description optophobia         {"name":"Optophobia",         "description":"opening one\'s eyes" }
HSET phobia_kind_description ornithophobia      {"name":"Ornithophobia",      "description":"birds" }
HSET phobia_kind_description orthophobia        {"name":"Orthophobia",        "description":"property" }
HSET phobia_kind_description ostraconophobia    {"name":"Ostraconophobia",    "description":"shellfish" }
HSET phobia_kind_description ouranophobia       {"name":"Ouranophobia",       "description":"heaven" }
HSET phobia_kind_description pagophobia         {"name":"Pagophobia",         "description":"ice or frost" }
HSET phobia_kind_description panophobia         {"name":"Panophobia",         "description":"everything" }
HSET phobia_kind_description panthophobia       {"name":"Panthophobia",       "description":"suffering and disease" }
HSET phobia_kind_description pantophobia        {"name":"Pantophobia",        "description":"everything" }
HSET phobia_kind_description papyrophobia       {"name":"Papyrophobia",       "description":"paper" }
HSET phobia_kind_description paralipophobia     {"name":"Paralipophobia",     "description":"neglect of responsibility" }
HSET phobia_kind_description parasitophobia     {"name":"Parasitophobia",     "description":"parasites" }
HSET phobia_kind_description parthenophobia     {"name":"Parthenophobia",     "description":"young girls" }
HSET phobia_kind_description pathophobia        {"name":"Pathophobia",        "description":"disease" }
HSET phobia_kind_description patroiophobia      {"name":"Patroiophobia",      "description":"heredity" }
HSET phobia_kind_description peccatophobia      {"name":"Peccatophobia",      "description":"sinning or imaginary crimes" }
HSET phobia_kind_description pediophobia        {"name":"Pediophobia",        "description":"dolls" }
HSET phobia_kind_description pedophobia         {"name":"Pedophobia",         "description":"children" }
HSET phobia_kind_description peladophobia       {"name":"Peladophobia",       "description":"bald people or baldness" }
HSET phobia_kind_description pellagrophobia     {"name":"Pellagrophobia",     "description":"pellagra" }
HSET phobia_kind_description peniaphobia        {"name":"Peniaphobia",        "description":"poverty" }
HSET phobia_kind_description pentheraphobia     {"name":"Pentheraphobia",     "description":"mother-in-law" }
HSET phobia_kind_description phagophobia        {"name":"Phagophobia",        "description":"swallowing or of eating or of being eaten" }
HSET phobia_kind_description phalacrophobia     {"name":"Phalacrophobia",     "description":"becoming bald" }
HSET phobia_kind_description pharmacophobia     {"name":"Pharmacophobia",     "description":"taking medicine" }
HSET phobia_kind_description pharmcophobia      {"name":"Pharmcophobia",      "description":"drugs" }
HSET phobia_kind_description phasmophobia       {"name":"Phasmophobia",       "description":"ghosts" }
HSET phobia_kind_description phengophobia       {"name":"Phengophobia",       "description":"daylight or sunshine" }
HSET phobia_kind_description phenogophobia      {"name":"Phenogophobia",      "description":"daylight" }
HSET phobia_kind_description philematophobia    {"name":"Philematophobia",    "description":"kissing" }
HSET phobia_kind_description philophobia        {"name":"Philophobia",        "description":"falling in love or being in love" }
HSET phobia_kind_description philosophobia      {"name":"Philosophobia",      "description":"philosophy" }
HSET phobia_kind_description phobophobia        {"name":"Phobophobia",        "description":"phobias" }
HSET phobia_kind_description phonophobia        {"name":"Phonophobia",        "description":"noises or voices" }
HSET phobia_kind_description photalgiophobia    {"name":"Photalgiophobia",    "description":"photalgin, the pain in the eyes caused by bright light" }
HSET phobia_kind_description photoaugliaphobia  {"name":"Photoaugliaphobia",  "description":"glaring lights" }
HSET phobia_kind_description photophobia        {"name":"Photophobia",        "description":"light" }
HSET phobia_kind_description phronemophobia     {"name":"Phronemophobia",     "description":"thinking" }
HSET phobia_kind_description phthiriophobia     {"name":"Phthiriophobia",     "description":"lice" }
HSET phobia_kind_description phthisiophobia     {"name":"Phthisiophobia",     "description":"tuberculosis" }
HSET phobia_kind_description placophobia        {"name":"Placophobia",        "description":"tombstones" }
HSET phobia_kind_description plutophobia        {"name":"Plutophobia",        "description":"wealth" }
HSET phobia_kind_description pluviophobia       {"name":"Pluviophobia",       "description":"rain or of being rained on" }
HSET phobia_kind_description pneumatophobia     {"name":"Pneumatophobia",     "description":"spirits or noncorporeal beings" }
HSET phobia_kind_description pnigophobia        {"name":"Pnigophobia",        "description":"choking" }
HSET phobia_kind_description pocrescophobia     {"name":"Pocrescophobia",     "description":"gaining weight" }
HSET phobia_kind_description pogonophobia       {"name":"Pogonophobia",       "description":"beards" }
HSET phobia_kind_description poinephobia        {"name":"Poinephobia",        "description":"punishment" }
HSET phobia_kind_description poliosophobia      {"name":"Poliosophobia",      "description":"contracting poliomyelitis" }
HSET phobia_kind_description politicophobia     {"name":"Politicophobia",     "description":"politicians" }
HSET phobia_kind_description polyphobia         {"name":"Polyphobia",         "description":"many things" }
HSET phobia_kind_description ponophobia         {"name":"Ponophobia",         "description":"overworking" }
HSET phobia_kind_description porphyrophobia     {"name":"Porphyrophobia",     "description":"the color purple" }
HSET phobia_kind_description potamophobia       {"name":"Potamophobia",       "description":"rivers or running water" }
HSET phobia_kind_description prosophobia        {"name":"Prosophobia",        "description":"progress" }
HSET phobia_kind_description psellismophobia    {"name":"Psellismophobia",    "description":"stuttering" }
HSET phobia_kind_description psychophobia       {"name":"Psychophobia",       "description":"mind" }
HSET phobia_kind_description pteronophobia      {"name":"Pteronophobia",      "description":"feathers" }
HSET phobia_kind_description pupaphobia         {"name":"Pupaphobia",         "description":"puppets" }
HSET phobia_kind_description pyrexiophobia      {"name":"Pyrexiophobia",      "description":"fever" }
HSET phobia_kind_description pyrophobia         {"name":"Pyrophobia",         "description":"fire" }
HSET phobia_kind_description radiophobia        {"name":"Radiophobia",        "description":"radiation, x-rays" }
HSET phobia_kind_description ranidaphobia       {"name":"Ranidaphobia",       "description":"frogs" }
HSET phobia_kind_description rhabdophobia       {"name":"Rhabdophobia",       "description":"being severely punished or criticized" }
HSET phobia_kind_description rhytiphobia        {"name":"Rhytiphobia",        "description":"getting wrinkles" }
HSET phobia_kind_description rupophobia         {"name":"Rupophobia",         "description":"dirt" }
HSET phobia_kind_description scabiophobia       {"name":"Scabiophobia",       "description":"scabies" }
HSET phobia_kind_description scelerophobia      {"name":"Scelerophobia",      "description":"criminals" }
HSET phobia_kind_description scholionophobia    {"name":"Scholionophobia",    "description":"school" }
HSET phobia_kind_description sciophobia         {"name":"Sciophobia",         "description":"shadows" }
HSET phobia_kind_description scoleciphobia      {"name":"Scoleciphobia",      "description":"worms" }
HSET phobia_kind_description scoptophobia       {"name":"Scoptophobia",       "description":"being seen or stared at" }
HSET phobia_kind_description scotomaphobia      {"name":"Scotomaphobia",      "description":"blindness in visual field" }
HSET phobia_kind_description scriptophobia      {"name":"Scriptophobia",      "description":"writing in public" }
HSET phobia_kind_description selachophobia      {"name":"Selachophobia",      "description":"sharks" }
HSET phobia_kind_description selaphobia         {"name":"Selaphobia",         "description":"light flashes" }
HSET phobia_kind_description selenophobia       {"name":"Selenophobia",       "description":"the moon" }
HSET phobia_kind_description septophobia        {"name":"Septophobia",        "description":"decaying matter" }
HSET phobia_kind_description sesquipedalophobia {"name":"Sesquipedalophobia", "description":"long words" }
HSET phobia_kind_description siderophobia       {"name":"Siderophobia",       "description":"stars" }
HSET phobia_kind_description sinistrophobia     {"name":"Sinistrophobia",     "description":"things to the left or left-handed" }
HSET phobia_kind_description soceraphobia       {"name":"Soceraphobia",       "description":"parents-in-law" }
HSET phobia_kind_description sociophobia        {"name":"Sociophobia",        "description":"society or people in general" }
HSET phobia_kind_description somniphobia        {"name":"Somniphobia",        "description":"sleep" }
HSET phobia_kind_description sophophobia        {"name":"Sophophobia",        "description":"learning" }
HSET phobia_kind_description soteriophobia      {"name":"Soteriophobia",      "description":"dependence on others" }
HSET phobia_kind_description spacephobia        {"name":"Spacephobia",        "description":"outer space" }
HSET phobia_kind_description spectrophobia      {"name":"Spectrophobia",      "description":"specters or ghosts" }
HSET phobia_kind_description spheksophobia      {"name":"Spheksophobia",      "description":"wasps" }
HSET phobia_kind_description stasiphobia        {"name":"Stasiphobia",        "description":"standing or walking" }
HSET phobia_kind_description stenophobia        {"name":"Stenophobia",        "description":"narrow things or places" }
HSET phobia_kind_description stygiophobia       {"name":"Stygiophobia",       "description":"hell" }
HSET phobia_kind_description symbolophobia      {"name":"Symbolophobia",      "description":"symbolism" }
HSET phobia_kind_description symmetrophobia     {"name":"Symmetrophobia",     "description":"symmetry" }
HSET phobia_kind_description syngenesophobia    {"name":"Syngenesophobia",    "description":"relatives" }
HSET phobia_kind_description syphilophobia      {"name":"Syphilophobia",      "description":"syphilis" }
HSET phobia_kind_description tabophobia         {"name":"Tabophobia",         "description":"a wasting sickness" }
HSET phobia_kind_description tachophobia        {"name":"Tachophobia",        "description":"speed" }
HSET phobia_kind_description taphophobia        {"name":"Taphophobia",        "description":"graves or being buried alive" }
HSET phobia_kind_description tapinophobia       {"name":"Tapinophobia",       "description":"being contagious" }
HSET phobia_kind_description taurophobia        {"name":"Taurophobia",        "description":"bulls" }
HSET phobia_kind_description technophobia       {"name":"Technophobia",       "description":"technology" }
HSET phobia_kind_description teleophobia        {"name":"Teleophobia",        "description":"definite plans or religious ceremony" }
HSET phobia_kind_description teniophobia        {"name":"Teniophobia",        "description":"tapeworms" }
HSET phobia_kind_description teratophobia       {"name":"Teratophobia",       "description":"bearing a deformed child" }
HSET phobia_kind_description testophobia        {"name":"Testophobia",        "description":"taking tests" }
HSET phobia_kind_description tetanophobia       {"name":"Tetanophobia",       "description":"lockjaw, tetanus" }
HSET phobia_kind_description textophobia        {"name":"Textophobia",        "description":"certain fabrics" }
HSET phobia_kind_description thaasophobia       {"name":"Thaasophobia",       "description":"being idle" }
HSET phobia_kind_description thalassophobia     {"name":"Thalassophobia",     "description":"the sea" }
HSET phobia_kind_description thanatophobia      {"name":"Thanatophobia",      "description":"death or dying" }
HSET phobia_kind_description theatrophobia      {"name":"Theatrophobia",      "description":"theatres" }
HSET phobia_kind_description theologicophobia   {"name":"Theologicophobia",   "description":"theology" }
HSET phobia_kind_description theophobia         {"name":"Theophobia",         "description":"gods or religion" }
HSET phobia_kind_description thermophobia       {"name":"Thermophobia",       "description":"heat" }
HSET phobia_kind_description thixophobia        {"name":"Thixophobia",        "description":"touching" }
HSET phobia_kind_description tokophobia         {"name":"Tokophobia",         "description":"pregnancy" }
HSET phobia_kind_description tomophobia         {"name":"Tomophobia",         "description":"surgical operations" }
HSET phobia_kind_description topophobia         {"name":"Topophobia",         "description":"performing" }
HSET phobia_kind_description toxiphobia         {"name":"Toxiphobia",         "description":"poison" }
HSET phobia_kind_description traumatophobia     {"name":"Traumatophobia",     "description":"injury" }
HSET phobia_kind_description tremophobia        {"name":"Tremophobia",        "description":"trembling" }
HSET phobia_kind_description trichopathophobia  {"name":"Trichopathophobia",  "description":"diseases of hair" }
HSET phobia_kind_description trichophobia       {"name":"Trichophobia",       "description":"hair" }
HSET phobia_kind_description triskaidekaphobia  {"name":"Triskaidekaphobia",  "description":"the number 13" }
HSET phobia_kind_description tropophobia        {"name":"Tropophobia",        "description":"moving or making changes" }
HSET phobia_kind_description trypanophobia      {"name":"Trypanophobia",      "description":"injections" }
HSET phobia_kind_description tyrannophobia      {"name":"Tyrannophobia",      "description":"tyrants" }
HSET phobia_kind_description vaccinophobia      {"name":"Vaccinophobia",      "description":"vaccines and vaccination" }
HSET phobia_kind_description venustraphobia     {"name":"Venustraphobia",     "description":"beautiful women" }
HSET phobia_kind_description verminophobia      {"name":"Verminophobia",      "description":"germs" }
HSET phobia_kind_description vermiphobia        {"name":"Vermiphobia",        "description":"earth worms" }
HSET phobia_kind_description vestiphobia        {"name":"Vestiphobia",        "description":"clothing" }
HSET phobia_kind_description vitricophobia      {"name":"Vitricophobia",      "description":"step-father" }
HSET phobia_kind_description wiccaphobia        {"name":"Wiccaphobia",        "description":"witches and witchcraft" }
HSET phobia_kind_description xanthophobia       {"name":"Xanthophobia",       "description":"the color yellow or the word yellow" }
HSET phobia_kind_description xenoglossophobia   {"name":"Xenoglossophobia",   "description":"foreign languages" }
HSET phobia_kind_description xenophobia         {"name":"Xenophobia",         "description":"strangers or foreigners" }
HSET phobia_kind_description xerophobia         {"name":"Xerophobia",         "description":"dryness and dry places, esp deserts" }
HSET phobia_kind_description xylophobia         {"name":"Xylophobia",         "description":"forests" }
HSET phobia_kind_description xyrophobia         {"name":"Xyrophobia",         "description":"razors" }
HSET phobia_kind_description zelophobia         {"name":"Zelophobia",         "description":"jealousy" }
HSET phobia_kind_description zeusophobia        {"name":"Zeusophobia",        "description":"a god or gods" }
HSET phobia_kind_description zoophobia          {"name":"Zoophobia",          "description":"animals" }
