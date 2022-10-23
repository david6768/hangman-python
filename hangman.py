import random
import time

words = ['abnormally','absentmindedly','accidentally','acidly','actually','adventurously','afterwards','almost','always','angrily','annually','anxiously','arrogantly','awkwardly','badly','bashfully','beautifully','bitterly','bleakly','blindly','blissfully','boastfully','boldly','bravely','briefly','brightly','briskly','broadly','busily	','calmly','carefully','carelessly','cautiously','certainly','cheerfully','clearly','cleverly','closely','coaxingly','colorfully','commonly','continually','coolly','correctly','courageously','crossly','cruelly','curiously','daily','daintily','dearly','deceivingly','delightfully','deeply','defiantly','deliberately','delightfully','diligently','dimly','doubtfully','dreamily','easily','elegantly','energetically','enormously','enthusiastically','equally','especially','even','evenly','eventually','exactly','excitedly','extremely','fairly','faithfully','famously','far','fast','fatally','ferociously','fervently','fiercely','fondly','foolishly','fortunately','frankly','frantically','freely','frenetically','frightfully','fully','furiously','generally','generously','gently','gladly','gleefully','gracefully','gratefully','greatly','greedily','happily','hastily','healthily','heavily','helpfully','helplessly','highly','honestly','hopelessly','hourly','hungrily','immediately','innocently','inquisitively','instantly','intensely','intently','interestingly','inwardly','irritably	','jaggedly','jealously','joshingly','joyfully','joyously','jovially','jubilantly','judgmentally','justly','keenly','kiddingly','kindheartedly','kindly','knavishly','knottily','knowingly','knowledgeably','kookily','lazily','less','lightly','likely','limply','lively','loftily','longingly','loosely','lovingly','loudly','loyally','madly','majestically','meaningfully','mechanically','merrily','miserably','mockingly','monthly','more','mortally','mostly','mysteriously','naturally','nearly','neatly','needily','nervously','never','nicely','noisily','not','obediently','obnoxiously','oddly','offensively','officially','often','only','openly','optimistically','overconfidently','owlishly','painfully','partially','patiently','perfectly','physically','playfully','politely','poorly','positively','potentially','powerfully','promptly','properly','punctually','quaintly','quarrelsomely','queasily','queerly','questionably','questioningly','quicker','quickly','quietly','quirkily','quizzically','rapidly','rarely','readily','really','reassuringly','recklessly','regularly','reluctantly','repeatedly','reproachfully','restfully','righteously','rightfully','rigidly','roughly','rudely','sadly','safely','scarcely','scarily','searchingly','sedately','seemingly','seldom','selfishly','separately','seriously','shakily','sharply','sheepishly','shrilly','shyly','silently','sleepily','slowly','smoothly','softly','solemnly','solidly','sometimes','soon','speedily','stealthily','sternly','strictly','successfully','suddenly','surprisingly','suspiciously','sweetly','swiftly','sympathetically','tenderly','tensely','terribly','thankfully','thoroughly','thoughtfully','tightly','tomorrow','too','tremendously','triumphantly','truly','truthfully','ultimately','unabashedly','unaccountably','unbearably','unethically','unexpectedly','unfortunately','unimpressively','unnaturally','unnecessarily','utterly','upbeat','upliftingly','upright','upside-down','upward','upwardly','urgently','usefully','uselessly','usually','utterly','vacantly','vaguely','vainly','valiantly','vastly','verbally','very','viciously','victoriously','violently','vivaciously','voluntarily','warmly','weakly','wearily','well','wetly','wholly','wildly','willfully','wisely','woefully','wonderfully','worriedly','wrongly','yawningly','yearly','yearningly','yesterday','yieldingly','youthfully','zealously','zestfully','zestily','able','about','above','abuzz','ace','achy','acid','acned','acute','adept','adult','afire','afoot','afoul','aft','after','aged','agile','aging','aglow','ago','ahead','aided','airy','ajar','akin','alert','alien','alike','alive','all','alone','aloof','alpha','alto','amber','ample','angry','anti','antic','antsy','any','apart','apish','apt','arced','arch','arid','armed','ashen','ashy','askew','astir','atrip','attic','avian','avid','awake','aware','awash','away','awed','awful','awing','awned','awry','axial','azure','back','bad','baggy','baked','bald','balmy','bandy','bare','bared','basal','base','based','basic','bated','bats','batty','bay','beady','beamy','beat','beefy','beery','beige','bent','best','beta','bias','birch','bitty','black','blame','bland','blank','bleak','blear','blind','blond','blown','blue','bluff','blunt','boggy','bogus','bold','bone','boned','bonny','bony','boon','boozy','bored','born','boss','bossy','both','bound','bowed','boxed','boxy','brag','brash','brave','brief','briny','brisk','broad','broke','brown','brute','buff','buggy','built','bulgy','bulky','bully','bum','bumpy','burly','burnt','bush','bushy','bust','busty','busy','butch','calm','camp','campy','catty','cheap','chewy','chic','chief','civic','civil','clean','clear','cleft','close','cocky','cod','cold','color','comfy','comic','cool','coral','corny','cosy','coy','cozy','crazy','crisp','cross','cubic','cured','curly','curt','curvy','cushy','cut','cute','cyan','daft','daily','damn','damp','dandy','dank','dark','dated','dazed','dead','deaf','dear','deep','deft','deist','dense','dewy','dicey','dim','dingy','dinky','dire','dirt','dirty','dizzy','dodgy','domed','done','doped','dopey','dopy','dormy','dosed','down','downy','dozen','drab','drawn','dread','drear','dress','dried','droll','drunk','dry','dual','dud','due','dull','dumb','dummy','dusky','dusty','dyed','dying','each','eager','early','eased','east','easy','edged','edgy','eerie','eight','elder','elect','elfin','elite','empty','ended','epic','equal','even','every','evil','exact','extra','eyed','fab','faced','faded','faint','fair','fake','false','famed','fancy','far','fast','fat','fatal','fated','fazed','feral','few','fewer','fiery','fifth','fifty','filmy','final','fine','finer','fired','firm','first','fishy','fit','five','fixed','fizzy','flaky','flash','flat','fleet','flint','flip','fluid','flush','fly','foamy','focal','foggy','fond','fore','foul','found','four','foxy','frail','frank','free','fresh','fried','front','full','fumed','funky','funny','furry','fused','fussy','fuzzy','game','gaudy','gaunt','gawky','giant','giddy','gimpy','glad','glum','godly','going','gold','gone','good','gooey','goofy','gory','grand','great','green','grey','grim','grimy','gross','grown','gruff','gummy','gushy','gusty','gutsy','hairy','hale','half','halt','hammy','handy','happy','hard','hardy','harsh','hasty','hated','hazel','hazy','heard','heavy','hefty','held','here','hex','hexed','high','hilly','hind','hip','hired','hoar','hoary','hokey','holey','holy','home','homey','honey','horny','hot','huffy','huge','human','humid','hurt','husky','icky','icy','ideal','idle','iffy','ill','inane','inept','inert','inky','inner','ionic','irate','iron','jade','jaded','jaggy','jawed','jazzy','jet','joint','jolly','jowly','juicy','jumbo','jumpy','just','kempt','key','keyed','khaki','kin','kind','kinky','known','kooky','laced','lacy','laid','lame','lank','lanky','large','last','late','later','lax','lay','lazy','leafy','leaky','lean','least','left','legal','less','level','light','like','liked','limp','lined','lit','live','liver','livid','loamy','local','loco','lofty','lone','long','loony','loopy','loose','lossy','lost','loud','lousy','loved','low','lowly','loyal','lucid','lucky','lumpy','lunar','lurid','lush','lusty','lyric','macho','macro','mad','made','magic','main','major','male','mangy','manic','manly','many','mass','matt','matte','mauve','mealy','mean','meaty','meek','meet','mere','merry','messy','metal','micro','mild','milky','mimic','mined','mini','minor','mint','minty','minus','mired','mirky','misty','mixed','mock','mod','modal','model','moist','molar','moldy','mono','moody','moony','moot','moral','more','mossy','most','mothy','motor','mousy','moved','mown','much','mucky','muddy','muggy','mum','mural','murky','mushy','musky','must','musty','mute','muted','naive','nary','nasal','nasty','natal','natty','naval','near','neat','needy','nervy','new','newsy','next','nice','nifty','nigh','nine','ninth','noble','noisy','none','north','nosed','noted','novel','nubby','numb','nuts','nutty','oaken','oaten','obese','odd','oiled','oily','okay','old','olden','older','olive','one','only','oozy','open','optic','oral','other','out','outer','oval','over','overt','owing','own','owned','pagan','paid','pale','palmy','pass','past','pasty','pat','paved','peaky','peaty','pedal','pent','peppy','perky','pert','pesky','pet','petty','phony','piano','picky','pied','piggy','pilar','pink','plain','plane','plumb','plump','plus','plush','polar','poor','pop','port','posed','posh','potty','pricy','prim','prior','privy','prize','prone','proof','prosy','proud','pubic','pudgy','puff','puffy','pulpy','punk','puny','pupal','pure','pushy','quack','quasi','quick','quiet','rabid','radio','rainy','rapid','rare','rash','raspy','ratty','raw','ready','real','rear','red','regal','retro','rich','rife','right','rigid','riled','ripe','risen','risky','ritzy','roast','robed','rocky','roomy','ropey','rose','rosy','rough','round','rowdy','royal','ruby','rude','ruled','rum','rummy','runic','runny','runty','rural','rush','rushy','rust','rusty','rutty','sad','safe','sage','said','salt','salty','same','sandy','sane','sappy','sassy','saute','saved','scaly','scant','scary','scrub','seamy','sear','seedy','self','sent','seven','sewed','sewn','shady','shaky','sham','sharp','shed','sheer','shiny','short','shot','showy','shut','shy','sick','side','sign','silky','silly','silty','sissy','six','sixth','sixty','size','sized','skew','skim','slack','slain','slaty','slav','sleek','slick','slim','slimy','slow','sly','small','smart','smoky','smug','snaky','sneak','snide','snowy','snub','snuff','snug','soapy','sober','soft','soggy','solar','sold','sole','solid','solo','some','sooty','sore','sorry','sound','soupy','sour','south','sown','spare','spent','spicy','spiky','spiny','splay','split','spry','spumy','squab','squat','stagy','stale','star','stark','steep','stern','stiff','still','stock','stone','stony','stout','straw','stray','stuck','stung','suave','such','sudsy','sulky','sunk','sunny','super','sure','surly','sweet','swell','swept','swift','swish','sworn','tabby','taboo','tacky','taken','talky','tall','tame','tamed','tan','tangy','taped','tardy','tart','tasty','tawny','teal','ten','tenor','tense','tenth','tepid','terse','testy','thick','thin','third','three','tidal','tidy','tied','tight','tiled','timed','timid','tinny','tiny','tipsy','tired','toed','token','tonal','toned','tonic','top','tops','torn','total','tough','toxic','tried','trig','trim','trite','true','tubby','tubed','tumid','twee','twin','two','ugly','ultra','uncut','under','undue','unfed','unfit','union','unlit','unwed','upper','upset','urban','used','usual','utter','vague','vain','valid','vapid','vast','viral','vital','vivid','vocal','void','wacky','warm','wary','washy','waste','wavy','waxed','waxen','waxy','weak','weary','weedy','weeny','weepy','weird','well','welsh','west','wet','whiny','white','whole','wide','wild','wily','wimpy','windy','wired','wiry','wise','wispy','witty','wonky','woody','wooly','woozy','wordy','wormy','worn','worse','worst','worth','wound','woven','wrong','wroth','wry','young','yucky','yummy','zany','zero','zesty','zippy','zonal','abide','accelerate','accept','accomplish','achieve','acquire','acted','activate','adapt','add','address','administer','admire','admit','adopt','advise','afford','agree','alert','alight','allow','altered','amuse','analyze','announce','annoy','answer','anticipate','apologize','appear','applaud','applied','appoint','appraise','appreciate','approve','arbitrate','argue','arise','arrange','arrest','arrive','ascertain','ask','assemble','assess','assist','assure','attach','attack','attain','attempt','attend','attract','audited','avoid','awake','back','bake','balance','ban','bang','bare','bat','bathe','battle','be','beam','bear','beat','become','beg','begin','behave','behold','belong','bend','beset','bet','bid','bind','bite','bleach','bleed','bless','blind','blink','blot','blow','blush','boast','boil','bolt','bomb','book','bore','borrow','bounce','bow','box','brake','branch','break','breathe','breed','brief','bring','broadcast','bruise','brush','bubble','budget','build','bump','burn','burst','bury','bust','buy','buze','calculate','call','camp','care','carry','carve','cast','catalog','catch','cause','challenge','change','charge','chart','chase','cheat','check','cheer','chew','choke','choose','chop','claim','clap','clarify','classify','clean','clear','cling','clip','close','clothe','coach','coil','collect','color','comb','come','command','communicate','compare','compete','compile','complain','complete','compose','compute','conceive','concentrate','conceptualize','concern','conclude','conduct','confess','confront','confuse','connect','conserve','consider','consist','consolidate','construct','consult','contain','continue','contract','control','convert','coordinate','copy','correct','correlate','cost','cough','counsel','count','cover','crack','crash','crawl','create','creep','critique','cross','crush','cry','cure','curl','curve','cut','cycle','dam','damage','dance','dare','deal','decay','deceive','decide','decorate','define','delay','delegate','delight','deliver','demonstrate','depend','describe','desert','deserve','design','destroy','detail','detect','determine','develop','devise','diagnose','dig','direct','disagree','disappear','disapprove','disarm','discover','dislike','dispense','display','disprove','dissect','distribute','dive','divert','divide','do','double','doubt','draft','drag','drain','dramatize','draw','dream','dress','drink','drip','drive','drop','drown','drum','dry','dust','dwell','earn','eat','edited','educate','eliminate','embarrass','employ','empty','enacted','encourage','end','endure','enforce','engineer','enhance','enjoy','enlist','ensure','enter','entertain','escape','establish','estimate','evaluate','examine','exceed','excite','excuse','execute','exercise','exhibit','exist','expand','expect','expedite','experiment','explain','explode','express','extend','extract','face','facilitate','fade','fail','fancy','fasten','fax','fear','feed','feel','fence','fetch','fight','file','fill','film','finalize','finance','find','fire','fit','fix','flap','flash','flee','fling','float','flood','flow','flower','fly','fold','follow','fool','forbid','force','forecast','forego','foresee','foretell','forget','forgive','form','formulate','forsake','frame','freeze','frighten','fry','gather','gaze','generate','get','give','glow','glue','go','govern','grab','graduate','grate','grease','greet','grin','grind','grip','groan','grow','guarantee','guard','guess','guide','hammer','hand','handle','handwrite','hang','happen','harass','harm','hate','haunt','head','heal','heap','hear','heat','help','hide','hit','hold','hook','hop','hope','hover','hug','hum','hunt','hurry','hurt','hypothesize','identify','ignore','illustrate','imagine','implement','impress','improve','improvise','include','increase','induce','influence','inform','initiate','inject','injure','inlay','innovate','input','inspect','inspire','install','institute','instruct','insure','integrate','intend','intensify','interest','interfere','interlay','interpret','interrupt','interview','introduce','invent','inventory','investigate','invite','irritate','itch','jail','jam','jog','join','joke','judge','juggle','jump','justify','keep','kept','kick','kill','kiss','kneel','knit','knock','knot','know','label','land','last','laugh','launch','lay','lead','lean','leap','learn','leave','lecture','led','lend','let','level','license','lick','lie','lifted','light','lighten','like','list','listen','live','load','locate','lock','log','long','look','lose','love','maintain','make','man','manage','manipulate','manufacture','map','march','mark','market','marry','match','mate','matter','mean','measure','meddle','mediate','meet','melt','melt','memorize','mend','mentor','milk','mine','mislead','miss','misspell','mistake','misunderstand','mix','moan','model','modify','monitor','moor','motivate','mourn','move','mow','muddle','mug','multiply','murder','nail','name','navigate','need','negotiate','nest','nod','nominate','normalize','note','notice','number','obey','object','observe','obtain','occur','offend','offer','officiate','open','operate','order','organize','oriented','originate','overcome','overdo','overdraw','overflow','overhear','overtake','overthrow','owe','own','pack','paddle','paint','park','part','participate','pass','paste','pat','pause','pay','peck','pedal','peel','peep','perceive','perfect','perform','permit','persuade','phone','photograph','pick','pilot','pinch','pine','pinpoint','pioneer','place','plan','plant','play','plead','please','plug','point','poke','polish','pop','possess','post','pour','practice','praised','pray','preach','precede','predict','prefer','prepare','prescribe','present','preserve','preset','preside','press','pretend','prevent','prick','print','process','procure','produce','profess','program','progress','project','promise','promote','proofread','propose','protect','prove','provide','publicize','pull','pump','punch','puncture','punish','purchase','push','put','qualify','question','queue','quit','race','radiate','rain','raise','rank','rate','reach','read','realign','realize','reason','receive','recognize','recommend','reconcile','record','recruit','reduce','refer','reflect','refuse','regret','regulate','rehabilitate','reign','reinforce','reject','rejoice','relate','relax','release','rely','remain','remember','remind','remove','render','reorganize','repair','repeat','replace','reply','report','represent','reproduce','request','rescue','research','resolve','respond','restored','restructure','retire','retrieve','return','review','revise','rhyme','rid','ride','ring','rinse','rise','risk','rob','rock','roll','rot','rub','ruin','rule','run','rush','sack','sail','satisfy','save','saw','say','scare','scatter','schedule','scold','scorch','scrape','scratch','scream','screw','scribble','scrub','seal','search','secure','see','seek','select','sell','send','sense','separate','serve','service','set','settle','sew','shade','shake','shape','share','shave','shear','shed','shelter','shine','shiver','shock','shoe','shoot','shop','show','shrink','shrug','shut','sigh','sign','signal','simplify','sin','sing','sink','sip','sit','sketch','ski','skip','slap','slay','sleep','slide','sling','slink','slip','slit','slow','smash','smell','smile','smite','smoke','snatch','sneak','sneeze','sniff','snore','snow','soak','solve','soothe','soothsay','sort','sound','sow','spare','spark','sparkle','speak','specify','speed','spell','spend','spill','spin','spit','split','spoil','spot','spray','spread','spring','sprout','squash','squeak','squeal','squeeze','stain','stamp','stand','stare','start','stay','steal','steer','step','stick','stimulate','sting','stink','stir','stitch','stop','store','strap','streamline','strengthen','stretch','stride','strike','string','strip','strive','stroke','structure','study','stuff','sublet','subtract','succeed','suck','suffer','suggest','suit','summarize','supervise','supply','support','suppose','surprise','surround','suspect','suspend','swear','sweat','sweep','swell','swim','swing','switch','symbolize','synthesize','systemize','tabulate','take','talk','tame','tap','target','taste','teach','tear','tease','telephone','tell','tempt','terrify','test','thank','thaw','think','thrive','throw','thrust','tick','tickle','tie','time','tip','tire','touch','tour','tow','trace','trade','train','transcribe','transfer','transform','translate','transport','trap','travel','tread','treat','tremble','trick','trip','trot','trouble','troubleshoot','trust','try','tug','tumble','turn','tutor','twist','type','undergo','understand','undertake','undress','unfasten','unify','unite','unlock','unpack','untidy','update','upgrade','uphold','upset','use','utilize','vanish','verbalize','verify','vex','visit','wail','wait','wake','walk','wander','want','warm','warn','wash','waste','watch','water','wave','wear','weave','wed','weep','weigh','welcome','wend','wet','whine','whip','whirl','whisper','whistle','win','wind','wink','wipe','wish','withdraw','withhold','withstand','wobble','wonder','work','worry','wrap','wreck','wrestle','wriggle','wring','write','x-ray','yawn','yell','zip','zoom','ace','ache','acid','acme','acorn','acre','act','actor','add','adder','adept','advil','afro','agave','age','aged','agent','agony','ailey','aim','aioli','air','aisle','akron','alarm','album','ale','alert','algae','alias','alibi','alien','alley','alloy','ally','aloe','alpha','alps','altar','amber','amigo','amino','amish','ammo','amp','angel','anger','angle','angst','angus','anime','ankle','annex','anole','ant','ante','antic','anvil','ape','apex','aphid','apple','april','apron','aqua','arbor','arc','arch','area','arena','argon','argus','ark','arm','armor','arms','army','aroma','array','arrow','arson','art','ascot','aspen','asset','ate','atom','attic','audio','audit','auger','aunt','aunty','aura','auto','award','awe','awl','axe','axiom','axis','axle','azure','baby','back','bacon','bad','badge','bag','bagel','bail','bait','baker','bale','balk','ball','balm','ban','band','bane','banjo','bank','banks','bar','barb','bard','barge','bark','barn','baron','bars','base','bash','basic','basil','basin','basis','bass','bat','batch','bath','baton','bay','bayou','beach','bead','beads','beak','beam','bean','bear','beard','beast','beat','beats','bed','bee','beech','beef','beep','beer','beet','begin','beige','being','belch','bell','belly','belt','bench','bend','bends','bent','beret','berry','bet','beta','bevel','bevy','bias','bib','bible','bid','bidet','bike','biker','bill','bin','bind','bingo','biome','biped','birch','bird','birth','bison','bit','bite','biter','black','blade','blame','blank','blast','blaze','blend','blimp','blind','bling','blink','blip','bliss','blitz','bloat','blob','block','blog','bloke','blond','blood','bloom','blow','blue','blues','bluff','blur','blurb','blush','boa','boar','board','boast','boat','bod','body','bog','bogey','boil','bold','bolt','bomb','bond','bone','boner','bones','bong','bongo','bonus','boo','book','boom','boon','boost','boot','booth','booty','booze','bore','borer','born','boss','bot','botch','bound','bow','bowel','bowl','bowls','box','boxer','boy','bra','brace','brag','braid','brail','brain','brake','bran','brand','brass','brat','brave','bravo','brawl','brawn','bread','break','breed','brew','briar','bribe','brick','bride','brie','brief','brim','brine','brink','brit','brits','britt','broad','broil','brood','brook','broom','broth','brow','brown','brunt','brush','brute','buck','bud','buddy','budge','buff','bug','buggy','bugle','build','bulb','bulge','bulk','bull','bully','bum','bump','bun','bunch','bung','bunk','bunny','buns','bunt','buoy','bur','burn','burns','burp','burst','bus','bush','buss','bust','buy','buyer','buzz','bye','bylaw','byte','cab','cabin','cable','cabot','cache','caddy','cadet','cafe','cage','cager','cake','calf','call','calm','cam','camel','camp','can','canal','candy','cane','cap','cape','caper','car','carat','card','cards','care','caret','cargo','carp','carry','cart','case','cash','cask','cast','caste','cat','catch','caulk','cause','cave','cavil','caw','cease','cedar','cell','cello','cent','chaff','chain','chair','chalk','champ','chant','chaos','chap','chard','charm','chart','chase','chasm','chat','cheat','check','cheek','cheep','cheer','chef','chess','chest','chew','chic','chick','chief','child','chill','chime','chimp','chin','chip','chips','chirp','chit','chive','chock','choir','choke','choky','chomp','chop','chord','chore','chow','chuck','chug','chum','chump','chunk','churn','chute','cider','cigar','cinch','cite','city','clack','claim','clam','clamp','clams','clan','clang','clank','clap','clash','clasp','class','clay','clean','clear','cleat','cleft','clerk','click','cliff','climb','cling','clip','cloak','clock','clog','clone','close','clot','cloth','cloud','clout','clove','clown','club','cluck','clue','clump','clunk','coach','coal','coast','coat','cobra','cocoa','cod','code','cog','coil','coin','coke','cola','cold','colon','color','colt','coma','comb','combo','come','comet','comic','comma','conch','condo','cone','coney','conk','cook','cool','coot','cop','cope','copy','coral','cord','cords','core','cork','corn','corp','corps','cost','costs','cosy','cot','couch','cough','count','court','cove','coven','cover','cow','cowl','cows','cozy','crab','crabs','crack','craft','cramp','crane','crank','crash','crate','crawl','craze','crazy','creak','cream','cred','cree','creed','creek','creep','crepe','cress','crest','crew','crib','crime','crimp','crisp','croak','crock','crook','crop','cross','crow','crowd','crown','crud','crude','crumb','crush','crust','crux','cry','crypt','cub','cubby','cube','cubit','cue','cuff','cull','cult','cup','curb','curd','cure','curl','curry','curse','curve','cut','cyan','cycle','cynic','dab','daily','dairy','daisy','dame','damp','dance','dandy','dane','dare','dark','dart','darts','dash','data','date','dawn','day','days','daze','dead','deaf','deal','dean','dear','death','debit','debt','debut','decal','decay','deck','decor','decoy','deed','deeds','deep','deer','delay','deli','delta','demo','demon','denim','dent','depot','depth','derby','desk','detox','deuce','devil','dew','dial','diary','dibs','dice','diet','dig','digit','digs','dill','dime','diner','ding','dip','dirt','disc','disco','dish','disk','ditch','ditto','dive','diver','dock','dodge','dog','dogma','doll','dolly','dolt','dome','donor','donut','doom','door','dope','dork','dorm','dot','doubt','dough','dove','dowel','down','dozen','dozer','draft','drag','drain','drama','drape','draw','dread','dream','dress','drew','drier','drift','drill','drink','drip','drive','drone','drool','drop','drove','drug','druid','drum','dry','dryer','duck','duct','due','duel','duet','dug','dunce','dune','dunk','dusk','dust','duty','dye','dyer','dying','eager','eagle','ear','earth','ease','easel','east','eater','eats','echo','edge','eel','egg','eggs','ego','eight','elbow','elder','elect','elf','elite','elk','elm','elves','email','ember','empty','emu','end','enemy','entry','envy','epic','epoxy','equal','era','error','essay','eve','even','event','evil','exam','exile','exit','extra','eye','eyes','fable','face','facet','fact','fad','fade','faint','fair','fairy','faith','fake','fall','falls','fame','fan','fancy','fang','far','farce','fare','farm','fast','fat','fate','fault','favor','fawn','fax','fear','feast','feat','fed','fee','feed','feel','felt','femur','fence','fern','ferry','fetch','feud','fever','few','fib','fiber','field','fiend','fifth','fifty','fig','fight','file','filet','fill','film','filth','final','finch','find','fine','fire','firm','first','fish','fist','fit','five','fiver','fives','fix','fixer','fizz','flag','flair','flak','flake','flame','flank','flap','flaps','flare','flash','flask','flat','flats','flaw','flea','fleet','flesh','flex','flick','flier','flies','fling','flint','flip','flirt','float','flock','flood','floor','flop','floss','flour','flow','flu','flub','fluff','fluid','fluke','flume','flush','flute','flux','fly','flyer','foam','focus','fog','foil','fold','folk','folks','folly','font','food','fool','foot','force','forge','fork','form','fort','forth','forty','forum','foul','found','four','fowl','fox','foyer','frail','frame','frat','fraud','fray','freak','free','freon','fret','friar','fries','frill','frisk','frizz','frog','front','frost','froth','frown','fruit','fry','fryer','fudge','fuel','full','fume','fumes','fun','fund','funds','fungi','funk','funny','fur','fury','fuse','fuss','futon','fuze','fuzz','gag','gage','gain','game','gamma','gap','gape','gas','gash','gasp','gate','gates','gator','gauge','gavel','gawk','gaze','gear','gecko','geek','gel','gem','gene','genie','genoa','genre','gent','germ','ghost','ghoul','giant','gift','gild','gimp','gin','gipsy','girl','gist','give','given','giver','gizmo','glad','glade','gland','glans','glare','glass','glaze','gleam','glee','glide','glint','globe','gloom','glory','gloss','glove','glow','glue','gnat','gnome','goal','goat','going','gold','golem','golf','goner','goo','good','goof','goofy','goon','goose','goth','gouge','gown','grab','grace','grad','grade','graft','grail','grain','gram','grand','grant','grape','graph','grasp','grass','grate','grave','gravy','gray','graze','great','greed','green','grey','grid','grief','grill','grime','grin','grind','grip','gripe','grit','grits','groan','groom','gross','group','grove','growl','grub','gruel','grump','grunt','guard','guess','guest','guide','guild','guilt','gulch','gulf','gull','gulp','gum','gun','guppy','guru','gush','gust','gut','guts','guy','gym','habit','hack','hag','hail','hair','half','hall','halo','halt','ham','hand','hands','handy','hang','hare','harp','hash','haste','hat','hatch','hate','hater','haunt','have','haven','havoc','hawk','hay','haze','hazel','head','heap','heaps','heart','heat','heavy','hedge','heed','heel','heft','heir','helix','hell','hello','helm','help','hem','hemp','hen','herb','herd','here','hero','hex','hick','hide','high','hike','hiker','hill','hilt','hind','hinge','hint','hip','hippo','hippy','hire','hiss','hit','hitch','hive','hives','hoagy','hoard','hoax','hob','hobby','hobo','hog','hoist','hold','hole','home','honey','honk','honor','hoof','hook','hooks','hoop','hoops','hoot','hop','hope','hops','horde','horn','horse','hose','host','hotel','hound','hour','hours','house','howl','hub','hue','huff','hug','hula','hulk','hull','hum','human','humor','hump','humus','hunch','hunk','hunt','hurl','hurry','hurt','hush','husk','husky','hut','hydra','hyena','hymn','hype','ibis','ice','icing','icon','idea','ideal','idiom','idiot','idle','idler','idol','igloo','iglu','ill','image','imp','inch','index','info','ingot','ink','inlet','inn','input','intro','ion','iris','iron','irony','isle','issue','itch','ivory','ivy','jab','jack','jacks','jail','jam','jamb','jar','java','jaw','jay','jazz','jean','jeans','jeep','jeer','jello','jelly','jest','jet','jetty','jewel','jig','jive','job','jock','jog','join','joint','joist','joke','joker','jolly','jolt','joust','joy','judge','jug','juice','juke','jump','junk','junky','juror','jury','kale','kayak','kazoo','kebab','keen','keep','keg','kelp','key','kick','kid','kiddy','kiln','kilo','kilt','kin','kind','king','kiss','kit','kite','kitty','kiwi','knack','knee','kneel','knell','knife','knit','knob','knock','knot','know','koala','krill','lab','label','labor','lace','lack','lad','ladle','lady','lag','lair','lake','lamb','lame','lamp','lance','land','lane','lap','lapel','lapse','lard','large','larva','laser','lash','lass','lasso','last','lat','latch','latex','lathe','latte','laugh','lava','law','lawn','laws','lay','layer','layup','leach','lead','leaf','leak','lean','leap','lear','lease','leash','least','leave','ledge','leech','leeds','leek','leer','left','lefty','leg','lego','legs','lemon','lemur','lens','lent','let','level','lever','liar','libel','lick','lid','lie','lied','life','lift','light','like','lilac','limb','limbo','lime','limit','limp','line','linen','liner','link','links','lint','lion','lip','lisp','list','lit','liter','liver','llama','loach','load','loads','loaf','loan','lob','lobby','lobe','local','lock','lodge','loft','log','logic','logo','loner','look','loom','loon','loony','loop','loot','lord','loser','loss','lost','lot','lots','lotto','lotus','love','lover','low','lower','luck','lump','lunch','lung','lure','lush','lying','mace','macro','madam','mafia','magi','magic','magma','maid','mail','main','major','maker','male','malt','mam','mama','mamba','mambo','mamma','man','mane','mango','mania','manor','map','maple','march','mare','mark','marks','mars','marsh','mash','mask','mass','mast','mat','match','mate','mates','math','maths','max','maxim','may','mayo','mayor','maze','meal','mean','means','meat','medal','medic','meet','meld','melee','melon','melt','memo','men','mend','menu','meow','mercy','merit','mesh','mess','metal','meter','meth','metro','might','mile','milk','mill','mills','mimer','mimic','min','mince','mind','mine','miner','mini','mink','minor','mint','minus','miser','miss','mist','mite','miter','mitt','mix','mixer','moan','moat','mob','mocha','mock','mod','modal','mode','model','modem','mogul','mojo','molar','mold','mole','molt','mom','momma','mommy','money','monk','month','moo','mooch','mood','moody','moon','moose','mop','mope','moped','moral','morse','moss','motel','moth','motor','motto','mould','mound','mount','mouse','mouth','move','mover','movie','mow','mucus','mud','muff','mug','mulch','mule','mum','mummy','munch','mural','muse','mush','music','musk','must','mute','mutt','mylar','nacho','name','namer','names','nanna','nap','nasal','navy','neck','need','needy','neon','nepal','nerd','nerve','nest','net','news','newt','nick','niece','night','nine','niner','ninja','ninth','noble','nod','node','noise','nomad','none','nook','noon','noose','north','nose','notch','note','noun','nudge','nuke','nun','nurse','nut','nylon','oaf','oak','oar','oasis','oat','oates','oath','ocean','octet','odds','ode','odor','offer','ogre','oil','oiler','oink','okay','old','oldie','olive','omega','omen','one','onion','onset','ooze','open','optic','oral','orange','orb','orbit','orca','order','ore','oreo','organ','ounce','out','oval','oven','over','owl','owner','oxbow','oxen','ozone','pace','pacer','pack','pact','pad','page','pager','pail','pain','pains','paint','pair','pal','pale','palm','pan','panda','pane','panel','panic','pansy','pant','pants','papa','paper','par','park','parks','part','parts','party','pass','past','pasta','paste','pat','patch','path','patio','pause','pave','paw','pawn','pay','payer','peace','peach','peak','pear','pearl','pecan','pedal','peek','peel','peer','peg','pelt','pen','penny','perch','peril','perk','pesto','pet','petal','petty','phase','phone','photo','piano','pick','pie','piece','pier','pig','piggy','pigmy','pike','pile','piles','pill','pimp','pin','pinch','pine','ping','pink','pinky','pinot','pint','pipe','pit','pita','pitch','pitt','pity','pivot','pixel','pizza','place','plaid','plain','plan','plane','plank','plant','plate','play','plaza','plea','plier','plot','plow','ploy','pluck','plug','plum','plumb','plume','plump','plus','plush','plyer','pod','poem','poet','point','poke','poker','pole','poll','polls','pond','pong','pony','pooch','poof','pool','poor','pop','poppy','porch','pore','pork','port','pose','poser','post','pot','pouch','pound','power','prank','prawn','press','prey','price','pride','prime','prism','prize','pro','probe','prom','promo','proof','prop','props','prose','prowl','prune','pry','pub','puck','puff','pug','pull','pulp','pulse','puma','pump','pun','punch','punk','punks','punt','pup','pupil','puppy','purge','purse','push','put','putt','putty','quack','quad','quake','qualm','quart','queen','query','quest','quick','quid','quiet','quilt','quirk','quirt','quiz','quota','quote','race','racer','rad','radar','radio','raft','rafts','rag','rage','raid','rail','rails','rain','raise','rake','rally','ram','ramp','ranch','range','rank','rant','rap','rapid','rash','rat','rate','rates','ratio','raw','ray','razor','razz','reach','read','ready','real','realm','ream','rear','rebel','red','reed','reef','reek','reel','reign','relay','relic','rent','reply','reset','resin','rest','retro','revel','rhino','rhyme','rib','rice','ricer','rich','ride','rider','ridge','riff','rifle','rift','rig','right','rim','rind','ring','rings','rink','rinse','riot','rip','rise','riser','risk','rite','rival','river','roach','road','roads','roar','roast','robe','robin','robot','rock','rod','rodeo','rogue','role','roll','room','rooms','roost','root','roots','rope','rose','rot','rotor','rouge','rough','round','route','rover','row','rowdy','rower','royal','rub','rube','ruby','rug','rugby','ruin','rule','ruler','rum','rummy','rumor','run','rune','rung','runt','ruse','rush','rust','rut','saber','safe','sag','saga','sage','sail','saint','salad','sale','salem','sales','salon','salsa','salt','same','sand','sands','sang','sash','sass','sauce','sauna','save','saver','savor','saw','say','scale','scan','scar','scare','scarf','scene','scent','scold','scone','scoop','scope','score','scorn','scout','scrap','sea','seal','seam','seat','seats','sect','sedan','see','seed','seek','seer','self','sell','sense','serum','serve','servo','set','setup','seven','shack','shade','shake','sham','shame','shank','shape','shard','share','shark','sharp','shave','shawl','shed','sheep','sheet','shelf','shell','shift','shill','shim','shin','ship','shirt','shoe','shoes','shop','shore','shot','shove','show','shred','shrub','shrug','shy','sick','siege','sigh','sight','sign','silk','silks','silly','silo','sin','sink','sinus','sip','sir','siren','six','sixer','sixth','sixty','size','ski','skid','skier','skill','skim','skin','skip','skirt','skit','skull','skunk','sky','slab','slack','slag','slain','slam','slang','slant','slap','slash','slate','slave','slaw','sled','sleep','sleet','slew','slews','slice','slick','slide','slime','sling','slip','slit','slob','slope','slot','sloth','slug','slum','slump','slur','slush','smack','small','smart','smash','smear','smell','smelt','smile','smirk','smith','smock','smog','smoke','snack','snag','snail','snake','snap','snare','snarl','sneak','sniff','snipe','snore','snort','snot','snow','snug','soak','soap','soar','sob','sock','sofa','softy','soil','sole','solid','son','sonar','song','sonny','soot','sooth','sore','sort','soul','sound','soup','sour','south','spa','space','spade','spam','span','spar','spare','spark','spasm','spat','spawn','speed','spell','spelt','spice','spike','spill','spin','spit','spite','splat','split','spoil','spoke','spoof','spook','spool','spoon','spore','sport','spot','spots','spout','spray','spree','spud','spur','spurt','spy','squat','squid','stab','stack','staff','stag','stage','stain','stair','stake','stalk','stall','stamp','stand','star','stare','start','stash','state','stay','stays','steak','steal','steam','steed','steel','steer','stem','step','steps','stern','stew','stick','stiff','still','stilt','sting','stink','stint','stir','stock','stoic','stomp','stone','stool','stoop','stop','stops','store','stork','storm','story','stove','strap','straw','stray','strip','strum','strut','stub','stud','study','stuff','stump','stunt','style','sub','suds','sugar','suit','suite','sum','sumer','sun','sung','super','surf','surge','sushi','sutra','swab','swag','swamp','swan','swap','swarm','sway','sweat','sweep','sweet','swell','swift','swim','swine','swing','swipe','swirl','swish','syrup','table','tack','taco','tact','tad','taffy','tag','tail','tails','take','taker','tale','talk','talks','tall','tally','talon','tan','tank','tap','tape','taps','tar','tarp','tart','task','taste','taunt','tax','taxer','taxi','taxis','tea','teach','teal','team','tear','tears','tease','teen','teens','teeth','tell','temp','tempo','ten','tense','tent','tenth','term','terms','test','text','thaw','theft','theme','then','there','theta','thick','thief','thigh','thing','think','third','thorn','three','throw','thud','thug','thumb','tick','tide','tidy','tie','tier','tiger','tilde','tile','till','time','timer','times','timid','tin','tint','tip','tire','titan','title','toad','toady','toast','today','toe','toil','token','toll','tomb','tome','ton','tone','toner','tongs','tonic','tons','tool','toon','toot','tooth','top','topic','torch','torso','toss','total','tote','totem','touch','tough','tour','tours','tow','towel','tower','town','towny','toxin','toy','trace','track','trade','trail','train','trait','trap','trash','tray','tread','treat','tree','trek','trend','triad','trial','trick','trim','trio','trip','troll','troop','trot','trout','truce','truck','true','trump','trunk','trust','truth','try','tub','tuba','tube','tuck','tug','tulip','tummy','tumor','tuna','tune','tuner','tunic','turf','turn','tush','tusk','tutor','twine','twins','twirl','twist','two','tying','type','typo','udder','ulcer','uncle','union','unit','unity','upper','upset','urn','usage','use','user','usher','using','valet','valor','value','valve','van','vase','vat','vault','vegan','veil','vein','venom','vent','venue','verb','verge','vest','vet','vial','vibe','vibes','vice','video','view','vigil','vine','vinyl','viola','viper','virgo','virus','visit','visor','vista','vocal','vodka','vogue','voice','void','volt','vote','voter','vow','vowel','wacko','wad','wade','wader','wads','wafer','waft','wag','wage','wager','wages','wagon','wail','wain','waist','wait','wake','walk','wall','waltz','wane','want','war','ward','ware','warp','wart','wash','wasp','waste','watch','water','watt','watts','wave','waver','wax','way','ways','wear','weave','web','wed','wedge','week','weird','well','wells','welsh','west','wet','whack','whale','wharf','wheat','wheel','whey','whiff','while','whim','whip','whirl','whisk','white','who','whole','whore','why','wick','widow','width','wife','wig','wild','will','wilt','wimp','win','wince','winch','wind','wine','wing','wings','wink','wipe','wiper','wire','wise','wish','wit','witch','wits','woe','wolf','woman','womb','won','wood','woods','woof','wool','word','words','work','works','world','worm','worry','worse','worst','wort','worth','wound','wow','wrack','wrap','wrath','wreck','wring','wrist','wrong','yam','yard','yarn','yawn','yay','year','years','yeast','yell','yes','yeti','yield','yoga','yolk','young','youth','zap','zebra','zinc','zing','zip','zit','zone','zoo','zoom','zero','zany','whir','welt','whig','wand','twin','tribe','tilt','sword','spine','spear','site','shock','sent']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lives = 17

def hang():
    if lives == 0:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print(' /|\  |')
        print(' / \  |')
        print('     _|_')
        print('')

    elif lives == 1:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print(' /|\  |')
        print(' /    |')
        print('     _|_')
        print('')

    elif lives == 2:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print(' /|\  |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 3:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print(' /|   |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 4:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print('  |   |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 5:
        print('')
        print('  ____')
        print('  |   |')
        print('  o   |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 6:
        print('')
        print('  ____')
        print('  |   |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 7:
        print('')
        print('  ____')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 8:
        print('')
        print('   ___')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 9:
        print('')
        print('    __')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 10:
        print('')
        print('     _')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 11:
        print('')
        print('      ')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 12:
        print('')
        print('      ')
        print('       ')
        print('      |')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 13:
        print('')
        print('      ')
        print('       ')
        print('       ')
        print('      |')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 14:
        print('')
        print('      ')
        print('       ')
        print('       ')
        print('       ')
        print('      |')
        print('     _|_')
        print('')

    elif lives == 15:
        print('')
        print('      ')
        print('       ')
        print('       ')
        print('       ')
        print('       ')
        print('     _|_')
        print('')

    elif lives == 16:
        print('')
        print('      ')
        print('       ')
        print('       ')
        print('       ')
        print('       ')
        print('     _| ')
        print('')

    elif lives == 17:
        print('')
        print('      ')
        print('       ')
        print('       ')
        print('       ')
        print('       ')
        print('      | ')
        print('')

def easy():
    global lives
    guessed_letters = []
    wordnum = random.randint(0, len(words)-1)
    word = words[wordnum]
    lives = 18
    while lives > 0:
        blanknum = 0
        hiddennum = 0
        blankword = word
        while blanknum < len(alphabet):
            blankword = blankword.replace(alphabet[blanknum], '_')
            blanknum +=1
        hiddenword = blankword
        while hiddennum < len(guessed_letters):
            if guessed_letters[hiddennum] in word:
                wordlet = word.index(guessed_letters[hiddennum])
                hiddenword = hiddenword[0:wordlet] + guessed_letters[hiddennum] + hiddenword[wordlet+1: ]
            hiddennum +=1
        print(hiddenword)
        if '_' not in hiddenword:
            print('')
            print('VICTORY!')
            print('')
            break
        guess = str(input('Guess a letter:'))
        if guess in word:
            guessed_letters.append(guess)
            guessed_letter = alphabet.index(guess)
        elif guess not in word:
            lives -= 1
            hang()
            time.sleep(1)
        if lives == 0:
            print('')
            print('GAME OVER')
            print('')

def hard():
    global lives
    guessed_letters = []
    wordnum = random.randint(0, len(words)-1)
    word = words[wordnum]
    lives = 18
    while lives > 0:
        blanknum = 0
        hiddennum = 0
        blankword = word
        while blanknum < len(alphabet):
            blankword = blankword.replace(alphabet[blanknum], '_')
            blanknum +=1
        hiddenword = blankword
        while hiddennum < len(guessed_letters):
            if guessed_letters[hiddennum] in word:
                wordlet = word.index(guessed_letters[hiddennum])
                hiddenword = hiddenword[0:wordlet] + guessed_letters[hiddennum] + hiddenword[wordlet+1: ]
            hiddennum +=1
        print(hiddenword)
        if '_' not in hiddenword:
            print('')
            print('VICTORY!')
            print('')
            break
        guess = str(input('Guess a letter: '))
        if guess in word:
            guessed_letters.append(guess)
            guessed_letter = alphabet.index(guess)
        elif guess not in word:
            lives -= 1
            if lives == 5: lives = 0
            hang()
            time.sleep(1)
        if lives == 0:
            print('')
            print('GAME OVER')
            print('')

def setup():
    global difficulty

    print('[1] Easy')
    print('[2] Hard')

    difficulty = int(input('Set Difficulty: '))

game = True

while game == True:

    print('[1] Play')
    print('[2] Quit')

    select = int(input('Select: '))

    if select == 2:
        quit()
    else:
        pass

    setup()

    if difficulty == 1:
        easy()
    else:
        hard()
