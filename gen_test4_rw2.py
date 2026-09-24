# gen_test4_rw2.py - Practice Test 4 RW Module 2 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw2 = []

# 1-4 Advanced Words in Context
rw2.append(make_mcq(
    "t4-rw-m2-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Because the experimental results defied prevailing theoretical models, the physicist's keynote presentation provoked a _____ response from the audience: half the attendees applauded his audacity, while the other half denounced his methodologies as reckless.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["polarizing", "conciliatory", "monotonous", "negligible"],
    "A",
    "Choice A is correct. 'Polarizing' means causing sharp division into opposing factions. Half the audience applauding and half denouncing directly exemplifies a polarizing response."
))

rw2.append(make_mcq(
    "t4-rw-m2-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The eccentric composer was celebrated for his highly _____ orchestration, frequently scoring symphonies that combined traditional violins with typewriter keys, sirens, and amplified vacuum cleaner motors.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["idiosyncratic", "conventional", "placid", "austere"],
    "A",
    "Choice A is correct. 'Idiosyncratic' means distinctive, peculiar, or unique to an individual. Blending violins with sirens and typewriters is highly idiosyncratic."
))

rw2.append(make_mcq(
    "t4-rw-m2-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "In her treatise on algorithmic society, the sociologist argued that smartphones have become so _____ that even unhoused populations and remote rural cooperatives depend on mobile connectivity for essential social services.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["ubiquitous", "transitory", "obsolete", "prohibitive"],
    "A",
    "Choice A is correct. 'Ubiquitous' means present, appearing, or found everywhere. Smartphones being relied upon across all demographics and remote areas proves they are ubiquitous."
))

rw2.append(make_mcq(
    "t4-rw-m2-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The commodities trader was notorious for his _____ temperament, swinging impulsively from reckless euphoria during market rallies to paralyzing despair at the slightest downtick in crude oil futures.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["mercurial", "stoic", "circumspect", "dogmatic"],
    "A",
    "Choice A is correct. 'Mercurial' means subject to sudden or unpredictable changes of mood or mind. Swinging between euphoria and despair defines a mercurial temperament."
))

# 5-8 Cross-Text Connections & Structure
rw2.append(make_mcq(
    "t4-rw-m2-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Economist Dr. Gregory Park argues that a direct carbon tax is the most transparent and economically efficient mechanism to reduce greenhouse gas emissions: by fixing a predictable dollar price per ton of CO₂, firms are provided with a clear price signal that incentivizes long-term investments in green technologies.",
        "Policy analyst Dr. Leah Thorne contends that cap-and-trade emission credit markets are superior to carbon taxes because they establish a legally binding ecological ceiling on aggregate annual emissions. Under a carbon tax, wealthy corporations might simply absorb the tax as an operating cost and continue polluting, failing to guarantee physical emission reductions."
    ),
    "Based on the texts, how would Thorne (Text 2) most likely criticize Park's carbon tax proposal (Text 1)?",
    [
        "By arguing that a fixed tax rate fails to guarantee a hard quantitative limit on total greenhouse gas emissions.",
        "By asserting that cap-and-trade systems are significantly more difficult to monitor than income taxes.",
        "By proving that corporations always pass carbon tax costs directly to low-income consumers.",
        "By agreeing that carbon taxes produce more predictable market pricing than emission permits."
    ],
    "A",
    "Choice A is correct. Thorne explicitly points out that a carbon tax does not guarantee physical emission reductions because wealthy firms can just pay the tax, whereas cap-and-trade sets a hard ecological ceiling."
))

rw2.append(make_mcq(
    "t4-rw-m2-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Ralph Ellison's 1952 novel <i>Invisible Man</i> opens and closes with a nameless Black narrator living in an underground cellar illuminated by 1,369 lightbulbs powered by stolen electricity. <u>By framing the entire novel from this subterranean vantage point, Ellison establishes visibility not as a physical ocular state, but as a sociopolitical condition: the protagonist is unseen not because he lacks physical form, but because mainstream white society refuses to acknowledge his humanity.</u>",
    "Which choice best describes the function of the underlined sentence in the text as a whole?",
    [
        "It explains the metaphorical significance of the novel's underground setting and framing device.",
        "It summarizes the historical publishing reception of Ellison's novel in postwar America.",
        "It provides biographical context regarding Ellison's years studying music at the Tuskegee Institute.",
        "It criticizes early modernist literature for ignoring racial discrimination."
    ],
    "A",
    "Choice A is correct. The underlined sentence explicitly decodes the metaphor: explaining how the subterranean cellar frame establishes visibility as a sociopolitical condition of racial blindness."
))

rw2.append(make_mcq(
    "t4-rw-m2-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
    "In theoretical computer science, the P versus NP problem asks whether every computational problem whose solution can be verified in polynomial time (NP) can also be solved in polynomial time (P). <u>If P equals NP, it would imply that finding a mathematical proof or decrypting cryptographic keys is no more computationally difficult than merely checking a candidate solution, fundamentally revolutionizing cryptography, mathematics, and artificial intelligence overnight.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It articulates the profound real-world consequences that would follow from a mathematical proof that P equals NP.",
        "It presents experimental evidence proving that P and NP are distinct mathematical complexity classes.",
        "It outlines the history of RSA public-key cryptography from the 1970s to the present.",
        "It disputes the assertion that polynomial verification is faster than brute-force computation."
    ],
    "A",
    "Choice A is correct. The underlined sentence describes the enormous real-world ramifications (revolutionizing cryptography, proofs, and AI) if P equals NP."
))

rw2.append(make_mcq(
    "t4-rw-m2-q8", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Historian Dr. Alan Ward argues that the transatlantic telegraph cable, completed in 1866, was the decisive technological catalyst that inaugurated modern financial globalization by synchronizing stock prices between London and New York in minutes rather than weeks.",
        "Economic historian Dr. Maya Patel contends that while the submarine cable accelerated communication speed, true financial globalization was already entrenched decades earlier through steamship postal networks and multinational merchant banking credit syndicates like the House of Rothschild."
    ),
    "Based on the texts, how does Patel (Text 2) respond to Ward's thesis (Text 1)?",
    [
        "She argues that financial globalization was already established through earlier banking and maritime infrastructure prior to the telegraph cable.",
        "She denies that the transatlantic telegraph cable ever operated reliably across the Atlantic seabed.",
        "She proves that London stock prices were completely isolated from American market fluctuations until the 20th century.",
        "She contends that submarine telegraph cables increased shipping transport costs between Europe and America."
    ],
    "A",
    "Choice A is correct. Patel directly counters Ward by arguing that true financial globalization had already been established decades earlier via steamships and merchant banking syndicates."
))

# 9-14 Information and Ideas
table_t4_q9 = make_table(
    ["Ice Core Depth (m)", "Estimated Age (kyr BP)", "Atmospheric CO₂ (ppm)", "Temperature Anomaly (°C)"],
    [
        ["500", "25", "190", "-8.2"],
        ["1,200", "65", "210", "-6.5"],
        ["1,800", "125 (Interglacial)", "285", "+1.8"],
        ["2,400", "160 (Glacial Max)", "185", "-9.0"]
    ]
)
rw2.append(make_mcq(
    "t4-rw-m2-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Hard",
    table_t4_q9 + "<br>Paleoclimatologists analyzing Antarctic ice core bubbles hypothesize that historical atmospheric carbon dioxide concentrations are tightly coupled with global temperature anomalies, with peaks in CO₂ coinciding with warm interglacial periods.",
    "Which choice best uses data from the table to support the paleoclimatologists' hypothesis?",
    [
        "At an estimated age of 125 kyr BP (the interglacial peak), atmospheric CO₂ reached its highest level (285 ppm) while the temperature anomaly peaked at +1.8°C, whereas during glacial maxima (160 kyr BP), CO₂ dropped to 185 ppm and temperatures plunged to -9.0°C.",
        "Atmospheric CO₂ at 25 kyr BP was higher than at 160 kyr BP, proving that glacial cycles were independent of carbon concentrations.",
        "Ice core depth at 1,800 meters was greater than at 500 meters, which caused carbon dioxide to concentrate.",
        "Temperature anomalies remained negative across all four geological epochs sampled in the ice core."
    ],
    "A",
    "Choice A is correct. It directly shows the tight coupling between CO₂ and temperature: highest CO₂ (285 ppm) matching peak warm interglacial (+1.8°C), and lowest CO₂ (185 ppm) matching deepest glacial cold (-9.0°C)."
))

rw2.append(make_mcq(
    "t4-rw-m2-q10", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "In his analysis of ancient trade routes, archaeologist Dr. Karim Rostam argues that the Silk Road was not a single, continuous highway traversed by solitary merchants, but rather an interlocking relay network where goods passed through multiple regional middlemen across Central Asian oasis cities.",
    "Which excerpt from a 4th-century Sogdian merchant letter would most directly support Rostam's argument?",
    [
        "\"I delivered the fifty bolts of Chinese raw silk to the Samarkand caravan leader, who will transport them westward to the Persian frontier where another merchant will purchase them for Antioch.\"",
        "\"The Chinese emperor has banned all export of mulberry leaves and silkworm eggs under penalty of death.\"",
        "\"Our ship dropped anchor in the harbor of Alexandria after three months of uninterrupted sailing from Rome.\"",
        "\"The desert sandstorm destroyed twenty iron plows during our journey across the northern steppe.\""
    ],
    "A",
    "Choice A is correct. Delivering goods to a Samarkand caravan leader who hands them off to another merchant for the next leg perfectly exemplifies an interlocking relay network with middlemen."
))

rw2.append(make_mcq(
    "t4-rw-m2-q11", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Benthic marine ecologists studying 'whale falls'—the carcasses of deceased cetaceans that sink into the abyssal zone—found that these massive biological depositions create ephemeral ecological islands on the nutrient-poor ocean floor. In the initial mobile-scavenger phase, sleeper sharks and hagfish strip soft tissue over two years. In the subsequent opportunistic phase, worms and crustaceans colonize the sediment. In the final sulfophilic stage, which lasts over fifty years, anaerobic bacteria decompose bone lipids, producing hydrogen sulfide that fuels chemotrophic bacterial mats identical to those found at hydrothermal vents. Because whale falls occur randomly across thousands of miles of barren benthic plains, oceanographers suspect that whale falls _____.",
    "Which choice most logically completes the text?",
    [
        "serve as crucial evolutionary stepping stones that allow chemotrophic organisms to disperse across vast abyssal ocean basins",
        "are the exclusive dietary energy source for photosynthetic phytoplankton living in surface photic zones",
        "prevent deep-sea bottom waters from undergoing natural thermohaline circulation",
        "cause irreversible oceanic hypoxia across thousands of square kilometers of continental shelves"
    ],
    "A",
    "Choice A is correct. Producing hydrothermal-like chemotrophic sulfide communities scattered across barren abyssal plains explains how vent species disperse between distant vents across the deep ocean."
))

rw2.append(make_mcq(
    "t4-rw-m2-q12", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "The introduction of high-throughput sequencing has revolutionized metagenomics, enabling researchers to sample genetic material directly from environmental specimens without culturing microbes in laboratories. Previously, microbiologists suffered from the 'great plate count anomaly': less than one percent of all environmental bacterial species could be grown on agar petri dishes, leaving ninety-nine percent of microbial biodiversity scientifically invisible. Metagenomic shotgun sequencing bypasses this bottleneck by isolating all DNA extracted from a pinch of soil or drop of seawater, cataloging millions of previously uncharacterized genomes.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Metagenomic sequencing overcomes the limitation of culturing microbes on agar, revealing the vast majority of previously uncharacterized environmental biodiversity.",
        "Traditional agar petri dishes remain the most cost-effective method for cataloging rare oceanic viruses.",
        "Over ninety-nine percent of all bacterial species in soil have gone extinct over the last century.",
        "Shotgun sequencing can only be performed on microbes that have been isolated in pure laboratory cultures."
    ],
    "A",
    "Choice A is correct. The text explains that high-throughput metagenomics overcomes the 'great plate count anomaly' (<1% culturable), uncovering the 99% of microbial life that couldn't be cultured."
))

rw2.append(make_mcq(
    "t4-rw-m2-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In cognitive behavioral psychology, the 'framing effect' describes how cognitive decisions are influenced by whether outcomes are presented as potential gains or potential losses. In a famous experiment, participants were presented with a public health strategy to combat a disease outbreak expected to kill 600 people. When Option A was framed as '200 people will be saved,' 72 percent of participants chose it over a risky gamble. However, when the identical outcome was framed as '400 people will die,' only 22 percent chose Option A, preferring the risky gamble. This dramatic reversal indicates that human decision-making _____.",
    "Which choice most logically completes the text?",
    [
        "exhibits risk aversion when choices are framed as potential gains, but shifts toward risk-seeking when choices are framed as potential losses",
        "is guided exclusively by purely objective, mathematical expected-value calculations",
        "remains completely immune to linguistic phrasing when real human lives are at stake",
        "invariably prefers certain losses over probabilistic gambles in medical emergencies"
    ],
    "A",
    "Choice A is correct. Choosing the certain outcome when framed as lives saved (gains) and taking the gamble when framed as deaths (losses) proves people are risk-averse for gains and risk-seeking for losses."
))

rw2.append(make_mcq(
    "t4-rw-m2-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "The Treaty of Westphalia, signed in 1648 at the conclusion of the Thirty Years' War, established the conceptual cornerstone of modern international relations: Westphalian sovereignty. The peace accords codified the principle of <i>cuius regio, eius religio</i>, asserting that sovereign states have exclusive domestic jurisdiction over their territory and domestic affairs, legally prohibiting foreign intervention in internal religious and governance policies.",
    "According to the text, what fundamental principle was established by the Treaty of Westphalia?",
    [
        "Sovereign nation-states have exclusive domestic authority over their internal territory and governance, free from foreign interference.",
        "All European nations must belong to a single unified ecclesiastical council.",
        "International law mandates that democratic elections be conducted every four years.",
        "Mercantile trade routes across European borders must be regulated by a centralized imperial court."
    ],
    "A",
    "Choice A is correct. The text explicitly defines Westphalian sovereignty as the principle that sovereign states have exclusive domestic jurisdiction and are protected from foreign intervention."
))

# 15-21 Standard English Conventions
rw2.append(make_mcq(
    "t4-rw-m2-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
    "The urban development commission prioritized three infrastructure goals: Dr. Lin's plan to expand electric bus _____ Director Vance's project to restore waterfront mangrove parks; and Chief Engineer Patel's initiative to modernize storm sewers.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["corridors;", "corridors,", "corridors—", "corridors:"]
    ,"A",
    "Choice A is correct. In a list where individual items contain descriptive modifiers or internal punctuation, semicolons must separate the items."
))

rw2.append(make_mcq(
    "t4-rw-m2-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The lead biochemist explained that the newly discovered alkaloid—a complex nitrogenous compound extracted from Amazonian tree _____ had exhibited potent anti-inflammatory properties in preclinical trials.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["bark—", "bark,", "bark;", "bark"]
    ,"A",
    "Choice A is correct. An em-dash is required to close the parenthetical descriptor that began with '—a complex nitrogenous compound extracted from Amazonian tree bark—'."
))

rw2.append(make_mcq(
    "t4-rw-m2-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "The ongoing restoration of Renaissance frescos damaged during the catastrophic Florence flood of 1966 _____ an extraordinary synthesis of chemical engineering and art history.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["represents", "represent", "have represented", "are representing"],
    "A",
    "Choice A is correct. The singular head subject is 'The ongoing restoration', requiring the singular verb 'represents'."
))

rw2.append(make_mcq(
    "t4-rw-m2-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Hard",
    "Constructed from high-tensile titanium alloy and equipped with redundant gyroscopic stabilizers, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the deep-sea robotic arm withstood pressures exceeding one thousand atmospheres.",
        "engineers deployed the deep-sea robotic arm to withstand extreme hydrostatic pressures.",
        "extreme hydrostatic pressures could not deform the deep-sea robotic arm.",
        "it was possible for the deep-sea robotic arm to perform delicate subsea sampling."
    ],
    "A",
    "Choice A is correct. The introductory modifier 'Constructed from high-tensile titanium alloy...' must logically modify 'the deep-sea robotic arm'."
))

rw2.append(make_mcq(
    "t4-rw-m2-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "Early quantum chemists assumed that chemical bonds were rigid, static linkages between atoms; _____ spectroscopic analyses revealed that molecular bonds continuously vibrate, stretch, and bend.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["subsequently,", "furthermore,", "similarly,", "for example,"],
    "A",
    "Choice A is correct. 'Subsequently,' marks the historical advance that revised the early, inaccurate assumption."
))

rw2.append(make_mcq(
    "t4-rw-m2-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Every commercial airline must conduct comprehensive maintenance inspections on _____ aircraft prior to each scheduled departure.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["its", "their", "they're", "it's"],
    "A",
    "Choice A is correct. 'Every commercial airline' is singular, requiring the singular possessive pronoun 'its'."
))

rw2.append(make_mcq(
    "t4-rw-m2-q21", DOMAINS["RW"]["CONV"], "Parallel Structure", "Medium",
    "The new public health guidelines recommend that adults engage in regular aerobic exercise, maintain balanced dietary nutrition, and _____ seven to eight hours of restorative sleep each night.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["obtain", "obtaining", "to obtain", "obtains"],
    "A",
    "Choice A is correct. The parallel verb series consists of base verbs: 'engage...', 'maintain...', and 'obtain...'."
))

# 22-24 Transitions
rw2.append(make_mcq(
    "t4-rw-m2-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "Early medieval alchemists believed that base lead could be transmuted into gold through the philosopher's stone. _____, their laboratory experiments with distillation and metallurgy laid the foundational empirical techniques for modern scientific chemistry.",
    "Which choice completes the text with the most logical transition?",
    ["Nonetheless,", "Consequently,", "Similarly,", "For example,"],
    "A",
    "Choice A is correct. 'Nonetheless,' bridges the gap between their mistaken belief in gold transmutation and the genuine scientific value of their empirical distillation techniques."
))

rw2.append(make_mcq(
    "t4-rw-m2-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "The semiconductor fabrication plant requires an environment completely free of microscopic contaminants. _____, technicians must wear positive-pressure cleanroom suits and pass through high-velocity air showers before entering the facility.",
    "Which choice completes the text with the most logical transition?",
    ["To ensure this sterility,", "In contrast,", "Nevertheless,", "Conversely,"],
    "A",
    "Choice A is correct. Wearing suits and passing through air showers is the direct action taken to ensure the contaminant-free sterility stated in the first sentence."
))

rw2.append(make_mcq(
    "t4-rw-m2-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "The documentary film features stunning cinematic footage of Arctic polar landscapes. _____, it incorporates intimate interviews with indigenous elders whose traditional hunting routes are being disrupted by receding sea ice.",
    "Which choice completes the text with the most logical transition?",
    ["Just as powerfully,", "On the other hand,", "In other words,", "Instead,"],
    "A",
    "Choice A is correct. 'Just as powerfully,' introduces the emotional and cultural human interviews as an equally compelling complement to the stunning physical landscape cinematography."
))

# 25-27 Rhetorical Synthesis
rw2.append(make_mcq(
    "t4-rw-m2-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Antoni Gaudí was an acclaimed Catalan architect who designed Barcelona's Casa Batlló and Sagrada Família.",
        "He drew structural and aesthetic inspiration from organic natural forms rather than classical Greek columns.",
        "His columns resemble tree trunks that branch out at their crowns to support ceiling vaults.",
        "His exterior ceramic tiles mimic the scales and iridescent skin of marine organisms and reptiles.",
        "This approach created an architectural style known as Catalan Modernisme."
    ]),
    "The student wants to provide an example of how Gaudí integrated organic natural forms into his structural designs. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Exemplifying his organic design philosophy, Gaudí modeled the interior stone columns of his buildings after tree trunks that branch out at their crowns to support ceiling vaults.",
        "Antoni Gaudí was an acclaimed Catalan architect whose groundbreaking buildings defined the aesthetic of Catalan Modernisme.",
        "Gaudí designed celebrated Barcelona landmarks such as Casa Batlló and the towering basilica of the Sagrada Família.",
        "Catalan Modernisme was an architectural movement that departed from traditional Greek classical forms in the late 19th century."
    ],
    "A",
    "Choice A is correct. It directly fulfills the goal by giving the specific structural example (designing stone columns to branch out like tree trunks to support ceiling vaults)."
))

rw2.append(make_mcq(
    "t4-rw-m2-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "The Svalbard Global Seed Vault opened in 2008 in the remote Arctic archipelago of Svalbard, Norway.",
        "It acts as a secure backup genebank, safeguarding over 1.2 million seed crop samples from around the world.",
        "In 2015, the International Center for Agricultural Research in the Dry Areas (ICARDA) withdrew seeds from Svalbard.",
        "ICARDA's headquarters in Aleppo, Syria, had been damaged during the civil war, destroying its primary seed collection.",
        "Using the Svalbard backup samples, ICARDA successfully re-established its crop research in Lebanon and Morocco."
    ]),
    "The student wants to demonstrate the real-world humanitarian value of the Svalbard Global Seed Vault. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "When the Syrian civil war destroyed ICARDA's primary seed collection in Aleppo, the institution withdrew backup samples from Svalbard to successfully re-establish its essential crop research in Lebanon and Morocco.",
        "Opened in 2008 in Svalbard, Norway, the Svalbard Global Seed Vault holds over 1.2 million seed samples from across the globe.",
        "ICARDA is an international agricultural research institution dedicated to supporting crop breeding in arid dryland regions.",
        "The Svalbard Global Seed Vault serves as an international repository designed to safeguard agricultural diversity against catastrophic loss."
    ],
    "A",
    "Choice A is correct. It directly shows real-world humanitarian impact: replacing seeds destroyed in Syria so research could be re-established in Lebanon and Morocco."
))

rw2.append(make_mcq(
    "t4-rw-m2-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Synthetic nitrogen fertilizers were invented through the Haber-Bosch process in the early 20th century.",
        "The chemical reaction combines atmospheric nitrogen with hydrogen gas under high heat and pressure.",
        "Today, nitrogen fertilizers are credited with sustaining roughly 50 percent of the global human population.",
        "However, agricultural runoff washes excess nitrates into aquatic ecosystems, causing eutrophication and marine dead zones.",
        "The Haber-Bosch process also accounts for approximately 1.4 percent of global carbon dioxide emissions."
    ]),
    "The student wants to contrast the vital benefit of synthetic nitrogen fertilizers with an environmental drawback. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "While synthetic nitrogen fertilizers sustain roughly half of the global human population, agricultural runoff of excess nitrates causes severe aquatic eutrophication and marine dead zones.",
        "Invented in the early 20th century, the Haber-Bosch process combines atmospheric nitrogen and hydrogen gas under extreme pressure.",
        "The manufacturing of synthetic nitrogen fertilizers accounts for approximately 1.4 percent of global carbon dioxide emissions annually.",
        "Both marine eutrophication and atmospheric emissions are environmental consequences of modern agricultural chemical production."
    ],
    "A",
    "Choice A is correct. It directly contrasts the vital benefit (sustaining 50% of the world's population) with the environmental drawback (nitrate runoff causing eutrophication and dead zones)."
))

print(f"Test 4 RW Module 2 ready: {len(rw2)} questions.")
