"""08 Verb Patterns (B1-C2) - how each verb takes its complement.

A classic B2 error is treating every verb as if it always took 'to':
*I suggest to go / I insist to see. Every verb has a fixed pattern.
This is the highest-value module in the deck.
"""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge, serie

D = "08 Verb Patterns::"
D1, D2, D3, D4, D5 = D + "V + to + infinitive", D + "V + V-ing", \
    D + "V + Noun", D + "V + Object + Complement", \
    D + "Two Objects and V + Preposition"

# =========================================== VERBS + TO + INFINITIVE

serie(D1, [
    ["I need ___ to happen.", "need", "it needs to happen",
     "If the subject is the same person, use the <b>bare</b> form (no to); if it "
     "is someone else, <b>to + base</b>.",
     ex("<b>need to go</b> (I need to go) / <b>need you to go</b> (I need you to go).")],
    ["You must ___ to catch the train.", "hurry", "you must hurry",
     "<b>Modal + to + base</b>. The negative drops the <b>to</b>: "
     "<b>mustn't go</b>.",
     ex("You <b>mustn't be</b> late. / You <b>shouldn't go</b>.")],
    ["I'd like ___ some coffee, please.", "to have", "I would like to have",
     "<b>would like + to + base</b> = I would like.",
     ex("I'd <b>like to go</b>. / I <b>want to</b> stay.")],
    ["She agreed ___ the meeting.", "to cancel", "she agreed to cancel",
     "<b>agree + to + base</b>.",
     ex("She <b>agreed to pay</b>. / They <b>agreed on</b> a price (note the <b>on</b>!).")],
    ["He refused ___ help.", "to accept", "he refused to accept",
     "<b>refuse + to + base</b>. Note: <b>refuse + noun</b> = refuse a thing.",
     ex("He <b>refused to help</b>. / She <b>refused the offer</b>.")],
    ["They promised ___ back the money.", "to pay", "they promised to pay",
     "<b>promise + to + base</b>.",
     ex("He <b>promised to call</b>. / She <b>promised me the book</b>.")],
    ["I forgot ___ the keys.", "to lock", "I forgot to lock",
     "<b>forget + to + base</b> = forget TO DO something. "
     "<b>forget + V-ing</b> = forget that it already happened.",
     ex("I <b>forgot to lock</b> the door. / I <b>forgot locking</b> it (it's already locked).")],
    ["He denied ___ the charge.", "to pay", "he denied paying",
     "<b>deny + to + base</b> = deny being going to do. "
     "<b>deny + V-ing</b> = deny having done it.",
     ex("She <b>denied to pay</b>. / She <b>denied having stolen</b> it.")],
    ["The manager promised ___ a raise.", "to give", "he promised to give",
     "<b>promise + to + base</b> and also <b>promise + object + to + base</b>.",
     ex("He <b>promised me a raise</b> / <b>promised to give me a raise</b>.")],
    ["She learned ___ a new language.", "to speak", "she learned to speak",
     "<b>learn + to + base</b> = learn the skill. "
     "<b>learn about</b> = learn about a topic.",
     ex("I <b>learned to drive</b> at 17. / I'm <b>learning about</b> history.")],
], nivel="B1", tags=["verb-pattern to-infinitive"])

serie(D1, [
    ["He offered ___ us a lift.", "to drive", "he offered to drive",
     "<b>offer + to + base</b> and <b>offer + object + to + base</b>.",
     ex("She <b>offered to help</b>. / He <b>offered me a ride</b>.")],
    ["They agreed ___ a new price.", "on", "they agreed on a price",
     "For 'reaching an agreement', <b>agree on</b> + noun/gerund. For 'accepting a "
     "proposal', <b>agree to</b> + infinitive.",
     ex("We <b>agreed on</b> the price. / She <b>agreed to meet</b> at 8.")],
    ["She apologised ___ being late.", "for", "she apologised for being late",
     "<b>apologise for + V-ing</b>. Never <i>apologise to be late</i>.",
     ex("He <b>apologised for interrupting</b>. / I <b>apologised to her</b>.")],
    ["I congratulated her ___ the promotion.", "on", "I congratulated her on it",
     "<b>congratulate someone on something</b>.",
     ex("<b>Congratulations on</b> your new job! / I <b>congratulated him on</b> passing.")],
    ["He insisted ___ paying the bill.", "on", "he insisted on paying",
     "<b>insist on + V-ing</b>. <i>insist to pay</i> is WRONG.",
     ex("She <b>insisted on driving</b>. / He <b>insisted on paying</b>.")],
    ["She warned me ___ the dogs.", "about", "she warned me about the dogs",
     "<b>warn someone about/of something</b>.",
     ex("He <b>warned me about</b> the traffic. / <b>Warned me not to</b> touch it.")],
    ["They accused him ___ stealing.", "of", "they accused him of stealing",
     "<b>accuse someone of + V-ing</b>.",
     ex("She <b>accused him of lying</b>. / He was <b>accused of murder</b>.")],
    ["He blamed his manager ___ the mistake.", "for", "he blamed his manager for it",
     "<b>blame someone for something</b>.",
     ex("Don't <b>blame me for</b> that. / She <b>blamed him for</b> the delay.")],
    ["They succeeded ___ finding a solution.", "in", "they succeeded in finding",
     "<b>succeed in + V-ing</b>.",
     ex("He <b>succeeded in passing</b> the exam. / She <b>succeeded in convincing</b> them.")],
    ["She admitted ___ breaking the vase.", "to", "she admitted to breaking",
     "<b>admit + to + base</b> = admit having done. <b>admit of</b> is rare.",
     ex("He <b>admitted to stealing</b>. / She <b>admitted being wrong</b>.")],
    ["They apologised ___ the delay.", "for", "they apologised for the delay",
     "<b>apologise for + noun / V-ing</b>.",
     ex("We <b>apologised for the inconvenience</b>.")],
    ["I object ___ being treated like that.", "to", "I object to being treated",
     "<b>object to + noun / V-ing</b>.",
     ex("She <b>objected to being interrupted</b>. / They <b>objected to the plan</b>.")],
], nivel="B2", tags=["verb-pattern to-infinitive"])

# ======================================================= VERBS + V-ING

serie(D2, [
    ["I enjoy ___ football.", "playing", "I enjoy playing",
     "<b>enjoy / mind / finish / avoid / suggest / consider / imagine / admit / "
     "risk / deny / miss / can't help / feel like</b> + <b>V-ing</b>.",
     ex("I <b>enjoy reading</b>. / <s>I enjoy to read</s> WRONG.")],
    ["Would you mind ___ the window?", "opening", "would you mind opening",
     "<b>mind + V-ing</b> with <b>would</b> / <b>Do you mind + V-ing</b>.",
     ex("<b>Would you mind opening</b> it? / <s>Would you mind to open</s> WRONG.")],
    ["He suggested ___ a pizza.", "ordering", "he suggested ordering",
     "<b>suggest + V-ing</b> (no <i>to</i>). Also <b>suggest + that + clause</b>.",
     ex("She <b>suggested meeting</b> at 7. / He <b>suggested that we (should) go</b>.")],
    ["I don't mind ___ the meeting.", "postponing", "I don't mind postponing",
     "<b>don't mind + V-ing</b>.",
     ex("I <b>don't mind waiting</b>. / <b>Do you mind waiting?</b>")],
    ["I've stopped ___ coffee.", "drinking", "I've stopped drinking",
     "<b>stop + V-ing</b> = stop doing. <b>stop + to + base</b> = stop in order to do.",
     ex("He <b>stopped smoking</b>. / He <b>stopped to smoke</b> (he paused to smoke).")],
    ["She avoided ___ the question.", "answering", "she avoided answering",
     "<b>avoid + V-ing</b>.",
     ex("<b>Avoid touching</b> it. / <s>avoid to answer</s> WRONG.")],
    ["I can't help ___ about it.", "laughing", "I can't help laughing",
     "<b>can't help + V-ing</b> = cannot help it. "
     "<b>can't help but + V-ing</b> = cannot stop.",
     ex("I <b>can't help smiling</b>. / I <b>can't help but love</b> it.")],
    ["He denied ___ the email.", "sending", "he denied sending",
     "<b>deny + V-ing</b> = deny having done (past).",
     ex("She <b>denied taking</b> the money. / <b>Denied to take</b> is barely possible.")],
    ["They risked ___ the flight.", "cancelling", "they risked cancelling",
     "<b>risk + V-ing</b>.",
     ex("She <b>risked losing</b> her job. / <b>risked to lose</b> is rare.")],
    ["I feel like ___ something Chinese tonight.", "eating", "I feel like eating",
     "<b>feel like + V-ing</b>.",
     ex("I <b>feel like going</b> home. / <b>feel like to eat</b> is rare.")],
    ["He keeps ___ asking the same question.", "on", "he keeps on asking",
     "<b>keep + V-ing</b> with the idea of repeated action.",
     ex("She <b>keeps smiling</b>. / <b>kept + V-ing</b> = kept doing.")],
    ["Imagine ___ the reaction.", "seeing", "imagine seeing",
     "<b>imagine + V-ing</b>.",
     ex("<b>Imagine being</b> in his shoes. / <b>Imagine to see</b> does not exist.")],
], nivel="B2", tags=["verb-pattern -ing"])

# ====================================================== VERBS + NOUN

serie(D3, [
    ["She wanted ___ , not just friendship.", "a relationship", "she wanted a relationship",
     "Many verbs take a bare noun with no preposition: <b>want, need, buy, "
     "order, choose, take, make, do, have, get, find, pay, cost, owe, sell, "
     "book</b>.",
     ex("I <b>want a coffee</b>. / She <b>made a decision</b>. / <b>Do a favour</b>.")],
    ["He asked ___ .", "a favour", "he asked for a favour",
     "<b>ask for + noun</b> (for what you want). <b>ask + person</b> (who you ask).",
     ex("She <b>asked for a raise</b>. / He <b>asked me a question</b>.")],
    ["They referred ___ the manager.", "to", "they referred to the manager",
     "<b>refer to + person/abstract noun</b>.",
     ex("Don't <b>refer to</b> him as 'that guy'. / She <b>referred the case to</b> HR.")],
    ["He blamed ___ the weather for the delay.", "the weather on", "he blamed the weather",
     "<b>blame A for B</b> = blame A for B. With <b>for</b> if the 'culprit' is "
     "a situation.",
     ex("<b>Blame me for</b> that. / She <b>blamed her boss for</b> the error.")],
    ["She apologised ___ the mistake.", "for", "she apologised for the mistake",
     "<b>apologise for + V-ing / noun</b>.",
     ex("He <b>apologised for being late</b>. / I <b>apologised for the noise</b>.")],
    ["I took ___ of the fact that he was tired.", "notice", "I took notice",
     "<b>notice / be aware of / be aware that</b> = to notice.",
     ex("She <b>took no notice of</b> him. / <b>Are you aware of</b> the change?")],
    ["They make ___ use of renewable energy.", "use", "they make use",
     "<b>make use of</b> = take advantage of.",
     ex("We should <b>make use of</b> the free time.")],
    ["He paid ___ the bill.", "the bill", "he paid the bill",
     "<b>pay + noun</b> (no preposition) or <b>pay for + noun</b>.",
     ex("I <b>paid the rent</b>. / She <b>paid for my lunch</b>.")],
    ["The news ___ the public.", "shocked", "the news shocked the public",
     "<b>shock/surprise/please/frighten/disappoint + object</b>.",
     ex("The decision <b>shocked the public</b>. / She <b>frightened the children</b>.")],
    ["She objected ___ the proposal.", "to", "she objected to the proposal",
     "<b>object to</b>.",
     ex("Nobody <b>objected to</b> the plan.")],
], nivel="B2", tags=["verb-pattern noun"])

# ==================================== VERB + OBJECT + COMPLEMENT

serie(D4, [
    ["They elected him ___ .", "chairman", "they elected him chairman",
     "<b>Position verbs</b>: <b>elect, appoint, choose, name, make, consider, "
     "call</b> + <b>object + complement</b> (no <b>to</b>).",
     ex("They <b>made him president</b>. / We <b>elected her captain</b>.")],
    ["I found the film ___ .", "boring", "I found the film boring",
     "<b>Opinion/state verbs</b> = <b>find, consider, think, believe, feel, "
     "leave, keep</b> + <b>object + adjective</b>.",
     ex("I <b>found it easy</b>. / They <b>consider him clever</b>.")],
    ["The news made everyone ___ .", "worried", "the news made everyone worried",
     "<b>make + object + adjective</b> (no <i>to be</i> in the passive).",
     ex("The film <b>made me cry</b>. / It <b>made him happy</b>.")],
    ["She wants him ___ .", "to leave", "she wants him to leave",
     "<b>want/expect/ask/force/order/tell + object + to + base</b> (or <b>not "
     "to</b>).",
     ex("She <b>wanted me to stay</b>. / They <b>made him sign</b> (no <i>to</i>!).")],
    ["He got her ___ the contract.", "to sign", "he got her to sign",
     "<b>get/have/make + object + to + base</b> — <b>make</b> in the past is "
     "the exception (<b>made him sign</b>).",
     ex("I <b>got him to pay</b>. / She <b>had me write</b> a letter.")],
    ["They painted the wall ___ .", "yellow", "they painted the wall yellow",
     "<b>paint + object + colour</b> (no <b>to</b>).",
     ex("She <b>painted her nails red</b>. / They <b>painted the door white</b>.")],
    ["I like the kitchen ___ .", "clean and bright", "I like the kitchen clean",
     "<b>like/prefer + object + adjective</b>.",
     ex("I <b>like the film interesting</b>. / She <b>prefers it dark</b>.")],
    ["It kept me ___ all night.", "awake", "it kept me awake",
     "<b>keep + object + adjective/participle</b>.",
     ex("The noise <b>kept me awake</b>. / The story <b>kept him interested</b>.")],
], nivel="C1", tags=["verb-pattern object-complement"])

# ============================================= TWO-OBJECT VERBS

serie(D5, [
    ["She gave me ___ .", "some money", "she gave me some money",
     "<b>Two-object verbs</b> (transfer, desire, provision): <b>give, send, "
     "offer, lend, bring, show, teach, tell, buy, get, promise, deny, ask, owe, "
     "charge, hand, pass, read, throw, wish, want</b>.",
     ex("She <b>gave me some money</b>. / He <b>sent her a letter</b>.")],
    ["Can you lend me ___ ?", "your pen", "can you lend me your pen",
     "<b>lend someone something</b> (direct + indirect object).",
     ex("Can you <b>lend me your pen</b>? / She <b>lent me a book</b>.")],
    ["He promised her ___ .", "a car", "he promised her a car",
     "<b>promise someone something</b>.",
     ex("He <b>promised her a car</b>. / They <b>promised us a refund</b>.")],
    ["She taught us ___ .", "French", "she taught us French",
     "<b>teach someone something</b>. Note: it is the important verb that <b>can</b> "
     "also take <b>to</b> for the person: <b>teach someone to do something</b>.",
     ex("She <b>taught us French</b>. / She <b>taught us to dance</b>.")],
    ["He asked me ___ .", "a favour", "he asked me a favour",
     "<b>ask someone something</b>.",
     ex("He <b>asked me a question</b>. / She <b>asked me for help</b>.")],
    ["I bought my mother ___ .", "a necklace", "I bought my mother a necklace",
     "<b>buy someone something</b>.",
     ex("He <b>bought me a book</b>. / She <b>bought herself a car</b>.")],
    ["He told me ___ .", "the truth", "he told me the truth",
     "<b>tell someone something</b> (not <b>say something to someone</b>).",
     ex("He <b>told me a lie</b>. / <b>She said something to me</b>.")],
    ["She showed me ___ .", "her photos", "she showed me her photos",
     "<b>show someone something</b>. The direct object can be dropped: "
     "<b>show me</b> (show me how).",
     ex("She <b>showed me how to do it</b>. / Show <b>me</b>.")],
    ["He threw me ___ .", "the ball", "he threw me the ball",
     "<b>throw something at someone</b> (with <b>at</b> = at a person).",
     ex("He <b>threw the ball at me</b>. / She <b>threw a stone at the dog</b>.")],
    ["I wish you ___ .", "good luck", "I wish you good luck",
     "<b>wish someone something</b>. Also: <b>hope/want/expect</b>.",
     ex("I <b>wish you a happy birthday</b>. / She <b>wants us to leave</b>.")],
], nivel="B2", tags=["two-objects"])

# ============================================ VERB + FIXED PREPOSITION

gap(D5, "It depends ___ the weather.", "on", nivel="B2", cue="depend on",
    forma="depends on",
    regla="Verbs with an <b>obligatory</b> preposition. It cannot be dropped or "
          "changed.",
    ejemplos=ex("<b>depend on, rely on, count on, insist on, concentrate on, "
                "congratulate on, apologise for, account for</b>",
                "<i>It depends <s>from</s></i> is WRONG → <b>depends on</b>. In "
                "AmE you hear <i>depends upon</i>."),
    tags="verb-preposition")

gap(D5, "She apologized ___ being rude.", "for", nivel="B2",
    cue="apologise for", forma="apologised for",
    regla="The preposition goes with the <b>main verb</b>, not with the meaning.",
    ejemplos=ex("<b>apologise for + V-ing</b>", "<b>insist on + V-ing</b>",
                "<b>admit to + V-ing</b>", "<b>confess to + V-ing</b>",
                "Mnemonic for <b>-ing</b> after a preposition: <b>PREG</b> "
                "(Pardon, Regret, Excuse, Give up, Quit) + preposition + <b>-ing</b>."),
    tags="verb-preposition")

# =================================================================== CLOZE

cloze(D1, "I enjoy {{c1::playing}} football.",
      extra="<div class='box rule'><span class='lbl'>Verb pattern</span>"
            "These verbs take <b>-ing</b>: enjoy, mind, avoid, finish, suggest, "
            "consider, imagine, admit, deny, risk, miss, feel like, keep, "
            "can't help.</div>",
      tags="c1-c2 verb-pattern cloze")

cloze(D5, "She suggested {{c1::ordering}} a pizza.",
      extra="<div class='box warn'><span class='lbl'>suggest does NOT take to</span>"
            "<i>suggest to order</i> is WRONG. Correct: <b>suggest ordering</b> or "
            "<b>suggest that we order</b>.</div>",
      tags="c1-c2 verb-pattern cloze")
