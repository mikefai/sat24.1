# gen_test3_rw1.py - Practice Test 3 RW Module 1 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw1 = []

# 1-4 Words in Context
rw1.append(make_mcq(
    "t3-rw-m1-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Easy",
    "Although the renewable energy startup was still in its _____ phase, having developed only a single working prototype, venture capital investors pledged thirty million dollars in Series A funding.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["nascent", "obsolete", "culminating", "dormant"],
    "A",
    "Choice A is correct. 'Nascent' means newly developed, emerging, or in an early stage. Developing only a single working prototype describes an early, nascent stage."
))

rw1.append(make_mcq(
    "t3-rw-m1-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The diplomatic treaty established a _____ ceasefire along the disputed mountain border, but military observers warned that the cessation of hostilities remained fragile due to lingering nationalist tensions.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["tenuous", "perpetual", "resilient", "superfluous"],
    "A",
    "Choice A is correct. 'Tenuous' means weak, slight, or unsubstantial. The context mentions that the ceasefire was 'fragile' due to tensions, which directly corresponds to 'tenuous'."
))

rw1.append(make_mcq(
    "t3-rw-m1-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "In her critique of contemporary pop architecture, critic Sophia Vance praised the public library for eschewing _____ ornamentation in favor of clean, functional lines that prioritized natural illumination.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["gratuitous", "austere", "pragmatic", "subtle"],
    "A",
    "Choice A is correct. 'Gratuitous' means uncalled for, unjustified, or excessive. Eschewing gratuitous ornamentation means avoiding unnecessary, excessive decorative elements in favor of functionality."
))

rw1.append(make_mcq(
    "t3-rw-m1-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "Throughout his tenure, the university president maintained a _____ commitment to open inquiry, steadfastly defending controversial faculty symposia against vocal calls for ideological censorship.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["resolute", "capricious", "perfunctory", "equivocal"],
    "A",
    "Choice A is correct. 'Resolute' means admirably purposeful, determined, and unwavering. Steadfastly defending faculty against censorship illustrates a resolute commitment."
))

# 5-8 Cross-Text Connections & Structure
rw1.append(make_mcq(
    "t3-rw-m1-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Behavioral ecologist Dr. Carl Benson posits that cooperative breeding among Florida scrub jays is maintained through kin selection: non-breeding helper birds assist their parents in raising subsequent broods because indirect fitness gains from shared genetic heritage outweigh the uncertain odds of establishing an independent territory.",
        "Evolutionary biologist Dr. Anita Desai contends that helper behavior in scrub jays is primarily an ecological constraint response: extreme habitat saturation leaves young birds with virtually zero available unoccupied oak scrub territories, forcing them to remain philopatric and wait for inheritance opportunities rather than being driven by altruistic kin benefits."
    ),
    "Based on the texts, how does Desai (Text 2) view Benson's kin selection hypothesis (Text 1)?",
    [
        "She argues that helper behavior is driven by demographic land constraints and territory inheritance rather than predominantly by genetic altruism.",
        "She agrees that Florida scrub jays have abundant vacant territories available for independent breeding dispersal.",
        "She proves that helper birds are genetically unrelated to the breeding pairs they assist in nesting.",
        "She contends that scrub jays abandon their home territories within weeks of fledging."
    ],
    "A",
    "Choice A is correct. While Benson attributes helping to kin selection and shared genetics, Desai argues that ecological territory saturation forces birds to stay and wait for inheritance."
))

rw1.append(make_mcq(
    "t3-rw-m1-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Langston Hughes's 1926 essay 'The Negro Artist and the Racial Mountain' served as a definitive manifesto for the Harlem Renaissance. Hughes rejected the assimilationist impulse among black middle-class intellectuals who urged artists to mimic European aesthetic forms to gain mainstream approval. <u>Instead, Hughes insisted that authentic African American art must unapologetically celebrate the distinctive rhythms of jazz, blues, and Black vernacular speech, regardless of whether it pleased white patrons or conservative critics.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It articulates Hughes's affirmative artistic alternative to the assimilationist approach he rejected.",
        "It provides biographical details regarding Hughes's personal training in jazz musical theory.",
        "It summarizes the commercial reception of Hughes's poetry among European publishers.",
        "It criticizes contemporary Harlem Renaissance artists for neglecting musical performance traditions."
    ],
    "A",
    "Choice A is correct. After stating that Hughes rejected assimilationism, the underlined sentence states what Hughes argued artists should do instead (celebrate jazz, blues, and vernacular speech)."
))

rw1.append(make_mcq(
    "t3-rw-m1-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "In physics, the Casimir effect demonstrates that the quantum vacuum is not empty void, but rather a seething sea of virtual particles continuously popping in and out of existence. When two uncharged conducting metal plates are placed nanometers apart in a vacuum, fewer virtual wave modes can fit between the plates than in the open space outside them. This discrepancy creates a net inward pressure that pushes the two plates together, providing macroscopic physical evidence for quantum vacuum energy fluctuations.",
    "Which choice best states the primary purpose of the text?",
    [
        "To explain the theoretical basis and physical manifestation of the Casimir effect.",
        "To argue that classical Newtonian physics provides a superior description of vacuum mechanics.",
        "To outline the industrial manufacturing process used to construct metallic plates for particle colliders.",
        "To compare the gravitational attraction of conducting metals with electrostatic repulsion."
    ],
    "A",
    "Choice A is correct. The passage explains how quantum vacuum fluctuations create pressure between metal plates, detailing the theoretical mechanism and manifestation of the Casimir effect."
))

rw1.append(make_mcq(
    "t3-rw-m1-q8", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The clinical trial demonstrated that the novel monoclonal antibody was remarkably _____, successfully binding to viral surface spike proteins without eliciting adverse autoimmune reactions in test subjects.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["efficacious", "volatile", "deleterious", "quixotic"],
    "A",
    "Choice A is correct. 'Efficacious' means successful in producing an intended result; effective. Successfully binding viral proteins without adverse reactions shows the antibody was efficacious."
))

# 9-14 Information and Ideas
table_t3_q9 = make_table(
    ["Exoplanet", "Orbital Period (days)", "Mass (Earth Masses)", "Atmospheric Water Vapor Detection"],
    [
        ["Kepler-1649c", "19.5", "1.2", "Undetected"],
        ["TOI-700d", "37.4", "1.7", "Tentative"],
        ["K2-18b", "32.9", "8.6", "Confirmed (3.4σ)"],
        ["LHS 1140b", "24.7", "5.6", "Confirmed (4.1σ)"]
    ]
)
rw1.append(make_mcq(
    "t3-rw-m1-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Medium",
    table_t3_q9 + "<br>Astronomers utilizing transmission spectroscopy hypothesize that sub-Neptune exoplanets (masses between 4 and 10 Earth masses) are more likely to retain detectable atmospheric water vapor than terrestrial super-Earths (masses under 3 Earth masses).",
    "Which choice best uses data from the table to support the astronomers' hypothesis?",
    [
        "Both sub-Neptunes in the sample (K2-18b and LHS 1140b) exhibited confirmed water vapor detections, whereas neither of the lower-mass terrestrial planets (Kepler-1649c and TOI-700d) had confirmed detections.",
        "TOI-700d has a longer orbital period than Kepler-1649c, which explains why water vapor was tentatively observed.",
        "LHS 1140b has a shorter orbital period than K2-18b despite having lower planetary mass.",
        "Kepler-1649c retained more atmospheric hydrogen than any other exoplanet in the dataset."
    ],
    "A",
    "Choice A is correct. The hypothesis links sub-Neptunes (4-10 Earth masses) to water vapor retention. Showing that both sub-Neptunes (K2-18b at 8.6, LHS 1140b at 5.6) had confirmed detections while lower-mass planets did not directly supports this."
))

rw1.append(make_mcq(
    "t3-rw-m1-q10", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Neuroscientists investigating language acquisition in early childhood compared brain activation patterns in monolingual and simultaneous bilingual infants using functional near-infrared spectroscopy (fNIRS). When exposed to unfamiliar phonemes from foreign languages, monolingual 11-month-old infants showed neural perceptual narrowing, responding only to native language sounds. In contrast, bilingual 11-month-olds retained neural plasticity, showing robust left-hemisphere responses to novel non-native phonemes. This physiological difference suggests that _____.",
    "Which choice most logically completes the text?",
    [
        "bilingual auditory environments extend the developmental window of phonological flexibility in the infant brain",
        "monolingual infants permanently lose the capacity to acquire second languages in adulthood",
        "bilingual infants develop vocabulary at a significantly slower rate than monolingual peers",
        "fNIRS imaging cannot detect cortical blood flow changes associated with linguistic processing"
    ],
    "A",
    "Choice A is correct. Since bilingual infants still responded to novel phonemes at 11 months while monolinguals narrowed, bilingual exposure prolongs the plastic window of phonological flexibility."
))

rw1.append(make_mcq(
    "t3-rw-m1-q11", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Easy",
    "The open-field agricultural system that dominated medieval northwestern Europe organized arable village land into several large, unfenced fields divided into narrow, scattered strips. Each peasant family farmed strips dispersed across different fields rather than a single contiguous parcel. This intentional fragmentation functioned as risk-diversification: because microclimatic variations, frost pockets, and soil drainage differed across the village territory, scattering plots ensured that a localized crop failure in one low-lying patch would not starve an entire household.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Medieval peasants farmed scattered strips across village lands as an intentional strategy to hedge against localized agricultural risks.",
        "The open-field system was abandoned because contiguous family farms generated higher commercial crop yields.",
        "Soil drainage across northwestern Europe was uniform, rendering plot scattering purely ceremonial.",
        "Medieval feudal lords mandated plot fragmentation to prevent peasant families from establishing private land ownership."
    ],
    "A",
    "Choice A is correct. The passage explains that scattering strips across different areas was an intentional risk-diversification strategy to ensure localized disasters didn't wipe out a family's entire food supply."
))

rw1.append(make_mcq(
    "t3-rw-m1-q12", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "Historian David Armitage contends that the 1776 American Declaration of Independence was primarily intended not as an internal manifesto of domestic civil liberties, but as an international instrument designed to establish legal standing for foreign treaties and military alliances under the law of nations.",
    "Which statement from the Declaration of Independence would most directly support Armitage's argument?",
    [
        "\"That as Free and Independent States, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which Independent States may of right do.\"",
        "\"We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights.\"",
        "\"He has refused his Assent to Laws, the most wholesome and necessary for the public good.\"",
        "\"Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes.\""
    ],
    "A",
    "Choice A is correct. It directly declares sovereign powers under the law of nations ('contract Alliances, establish Commerce, levy War'), explicitly corroborating Armitage's international treaty thesis."
))

rw1.append(make_mcq(
    "t3-rw-m1-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In molecular genetics, microRNAs (miRNAs) are short non-coding RNA molecules that regulate gene expression post-transcriptionally by binding to complementary sequences on messenger RNA (mRNA) transcripts, typically causing mRNA degradation or translational repression. When researchers engineered mice with genetic knockouts of miR-133 (a muscle-specific miRNA), the mice developed severe cardiac hypertrophy and erratic ventricular arrhythmia. Notably, levels of the cardiac structural protein collagen remained normal, but intracellular calcium-handling pumps were severely downregulated. This finding indicates that miR-133 _____.",
    "Which choice most logically completes the text?",
    [
        "plays a vital role in modulating calcium homeostasis mechanisms required for healthy cardiac rhythm",
        "serves as the primary structural component of heart muscle connective tissue fibers",
        "causes ventricular arrhythmias whenever it is overexpressed in mammalian myocardium",
        "is responsible for translating ribosomal RNA into structural skeletal proteins"
    ],
    "A",
    "Choice A is correct. Loss of miR-133 caused severe downregulation of calcium pumps and ventricular arrhythmia, proving miR-133 is vital for regulating cardiac calcium homeostasis and rhythm."
))

rw1.append(make_mcq(
    "t3-rw-m1-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "In classical economics, Adam Smith's concept of the 'division of labor' is famously illustrated through the manufacturing of pins. Smith observed that a single untrained artisan attempting to craft pins alone could scarcely produce twenty pins in a day. However, when the manufacturing process was subdivided into eighteen distinct operations—straightening wire, cutting lengths, grinding points, and attaching pinheads—ten workers could produce over forty-eight thousand pins daily, demonstrating a monumental gain in productive efficiency.",
    "According to the text, what enabled the pin workshop to achieve immense productivity gains?",
    [
        "Subdividing the manufacturing process into specialized, sequential tasks assigned to different workers.",
        "Replacing manual hand tools with steam-powered automated assembly machinery.",
        "Employing hundreds of artisans to perform identical unspecialized metalworking tasks.",
        "Importing pre-sharpened wire spools from foreign metallurgical suppliers."
    ],
    "A",
    "Choice A is correct. The text explicitly highlights that dividing the process into eighteen distinct operations assigned across specialized workers caused the massive output surge."
))

# 15-21 Standard English Conventions
rw1.append(make_mcq(
    "t3-rw-m1-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "The restoration of the ancient Roman villa revealed vibrant floor _____ although centuries of moisture had dimmed the outer border, the central figurative scene remained remarkably intact.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["mosaics; although", "mosaics, although", "mosaics although", "mosaics: although"],
    "A",
    "Choice A is correct. 'The restoration... revealed vibrant floor mosaics' is an independent clause. The following sentence begins with a dependent concessive clause ('although centuries of moisture had dimmed the outer border') followed by a main clause ('the central figurative scene remained remarkably intact'). A semicolon properly joins the two independent structures."
))

rw1.append(make_mcq(
    "t3-rw-m1-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Easy",
    "Biochemists extracted the active compound from the bark of the Pacific yew _____ which had long been recognized in traditional medicine for its therapeutic properties.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["tree,", "tree;", "tree:", "tree"]
    ,"A",
    "Choice A is correct. A comma is required before the nonrestrictive relative clause 'which had long been recognized in traditional medicine...'."
))

rw1.append(make_mcq(
    "t3-rw-m1-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "The ongoing collection and curation of oral histories from immigrant textile workers _____ an invaluable archival resource for labor historians.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["constitutes", "constitute", "have constituted", "are constituting"],
    "A",
    "Choice A is correct. The singular head subject 'The ongoing collection and curation' treated as a singular unified archival activity (or the head noun 'collection') requires the singular verb 'constitutes'."
))

rw1.append(make_mcq(
    "t3-rw-m1-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Medium",
    "Having completed an arduous eight-hour climb through gale-force winds and blowing snow, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the mountaineers finally reached the summit ridge of Mount Rainier.",
        "the summit ridge of Mount Rainier was finally reached by the mountaineers.",
        "reaching the summit ridge of Mount Rainier was achieved by the mountaineers.",
        "it was a great relief for the mountaineers to reach the summit ridge."
    ],
    "A",
    "Choice A is correct. The introductory modifier 'Having completed an arduous eight-hour climb...' must logically modify 'the mountaineers'."
))

rw1.append(make_mcq(
    "t3-rw-m1-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "In 1905, Albert Einstein published his theory of special relativity; _____ his revolutionary explanation of the photoelectric effect won him the 1921 Nobel Prize in Physics.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["however, it was", "moreover, it was", "for example, it was", "consequently, it was"],
    "A",
    "Choice A is correct. 'However, it was' provides the classic contrast: although he is most famous for relativity, it was his photoelectric effect paper that actually earned the Nobel Prize."
))

rw1.append(make_mcq(
    "t3-rw-m1-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Before any pharmaceutical manufacturer can market a new therapeutic drug, _____ must demonstrate both efficacy and safety in randomized, double-blind clinical trials.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["it", "they", "we", "he"],
    "A",
    "Choice A is correct. The antecedent is 'pharmaceutical manufacturer' (singular, entity), so the singular pronoun 'it' is required."
))

rw1.append(make_mcq(
    "t3-rw-m1-q21", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The lead geotechnical engineer noted that the dam's retaining wall—a monumental structure composed of pre-stressed concrete and anchored _____ had developed no visible stress fractures.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["pilings—", "pilings,", "pilings;", "pilings"]
    ,"A",
    "Choice A is correct. An em-dash is required to close the parenthetical descriptor that began with '—a monumental structure composed of pre-stressed concrete and anchored pilings—'."
))

# 22-24 Transitions
rw1.append(make_mcq(
    "t3-rw-m1-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Easy",
    "Traditional lithium batteries degrade rapidly under exposure to freezing sub-zero temperatures. _____, aerospace engineers have designed internal resistive heating circuits that warm battery modules prior to orbital solar charging.",
    "Which choice completes the text with the most logical transition?",
    ["In response,", "Meanwhile,", "Furthermore,", "Likewise,"],
    "A",
    "Choice A is correct. Designing heating circuits is a direct engineering response/solution to the cold degradation issue described in the first sentence."
))

rw1.append(make_mcq(
    "t3-rw-m1-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "The city council initially projected that the municipal light rail extension would cost $450 million. _____, unexpected tunneling complications through granite bedrock escalated the final project expenditure to over $700 million.",
    "Which choice completes the text with the most logical transition?",
    ["Ultimately,", "Similarly,", "For instance,", "Consequently,"],
    "A",
    "Choice A is correct. 'Ultimately,' marks the contrast between the initial budget projection and the final actual outcome."
))

rw1.append(make_mcq(
    "t3-rw-m1-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Octopuses lack a rigid skeletal structure, allowing them to squeeze through crevices no wider than their eye sockets. _____, they can alter the color and texture of their skin in milliseconds to match complex seafloor topography.",
    "Which choice completes the text with the most logical transition?",
    ["In addition,", "However,", "On the other hand,", "Nonetheless,"],
    "A",
    "Choice A is correct. 'In addition,' introduces a second distinct biological capability (skin color/texture camouflage) that complements the physical flexibility described first."
))

# 25-27 Rhetorical Synthesis
rw1.append(make_mcq(
    "t3-rw-m1-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "James Baldwin was an acclaimed 20th-century American essayist and novelist.",
        "In 1948, disillusioned by racial prejudice in the United States, he moved to Paris, France.",
        "Living in Paris provided Baldwin with the critical geographic distance needed to analyze American society.",
        "In France, he completed his seminal semi-autobiographical debut novel, Go Tell It on the Mountain (1953).",
        "His Paris essays were collected in Notes of a Native Son (1955), exploring race, identity, and democracy."
    ]),
    "The student wants to explain how living abroad influenced Baldwin's literary career. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Relocating to Paris in 1948 provided James Baldwin with the critical distance necessary to examine American race relations, leading him to complete Go Tell It on the Mountain and Notes of a Native Son.",
        "In 1948, disillusioned by racial prejudice, James Baldwin moved to Paris, where he lived for many years as an expatriate writer.",
        "James Baldwin published his celebrated debut novel, Go Tell It on the Mountain, in 1953, followed by Notes of a Native Son in 1955.",
        "Notes of a Native Son is a landmark collection of essays written by James Baldwin that explores American identity and racial democracy."
    ],
    "A",
    "Choice A is correct. It directly addresses the prompt's focus: how living abroad influenced his career (providing distance that enabled him to analyze race and complete his landmark works)."
))

rw1.append(make_mcq(
    "t3-rw-m1-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Reykjavik, Iceland, is one of the world's most sustainable capital cities.",
        "Over 99 percent of the city's heating and hot water needs are met through geothermal district energy.",
        "Subterranean geothermal water is piped from nearby volcanic fields directly into municipal heating radiators.",
        "This system eliminates the need for fossil fuel combustion, preventing approximately 100 million metric tons of CO₂ emissions annually.",
        "Geothermal water is also circulated beneath city sidewalks to melt snow and ice during winter."
    ]),
    "The student wants to emphasize an urban infrastructure benefit of Reykjavik's geothermal system beyond residential heating. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Beyond heating over 99 percent of homes, Reykjavik's geothermal water is routed beneath municipal sidewalks to automatically melt winter snow and ice.",
        "Piping subterranean geothermal water from volcanic fields into homes prevents an estimated 100 million metric tons of CO₂ emissions each year.",
        "Reykjavik, Iceland, is celebrated worldwide for meeting virtually all of its municipal energy and heating demands through clean geothermal power.",
        "Geothermal district heating utilizes subterranean hot water rather than fossil fuels to provide residential heat."
    ],
    "A",
    "Choice A is correct. The prompt asks for an urban infrastructure benefit beyond residential heating, which choice A explicitly delivers (melting sidewalk snow and ice)."
))

rw1.append(make_mcq(
    "t3-rw-m1-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Anhydrobiosis is a state of suspended animation entered by organisms undergoing severe desiccation.",
        "When drying out, tardigrades synthesize unique tardigrade disordered proteins (TDPs).",
        "TDPs lack a fixed three-dimensional structure in hydrated conditions.",
        "As water evaporates, TDPs undergo liquid-to-solid phase transition, forming protective bioglass matrices.",
        "These bioglass matrices lock essential cellular enzymes in place, preventing denaturing."
    ]),
    "The student wants to describe what happens to TDPs as cellular water evaporates. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "As cellular water evaporates, TDPs undergo a liquid-to-solid phase transition to form protective bioglass matrices that immobilize and protect vital enzymes.",
        "Tardigrades enter a state of suspended animation known as anhydrobiosis when deprived of environmental moisture.",
        "Under hydrated conditions, tardigrade disordered proteins lack a fixed three-dimensional physical structure.",
        "Tardigrade disordered proteins are unique biopolymers that enable microscopic organisms to endure desiccation."
    ],
    "A",
    "Choice A is correct. It specifically answers the prompt by describing what happens as water evaporates (TDPs undergo phase transition into bioglass matrices that protect enzymes)."
))

print(f"Test 3 RW Module 1 ready: {len(rw1)} questions.")
