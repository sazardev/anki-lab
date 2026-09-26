"""15 Common Errors (B2-C2) - interference from other languages, classic B1
mistakes, B2-C1 mistakes, and spelling/pronunciation traps."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "15 Common Errors::"
E1, E2, E3, E4 = D + "L1 Interference", D + "Classic B1 Errors", \
    D + "B2-C1 Errors", D + "Spelling and Pronunciation"

# ================================================== L1 INTERFERENCE

serie_gap(E1, [
    ("I'm looking forward ___ the weekend.", "to", "look forward to",
     "ERROR: 'look forward to + V'. Correct: <b>look forward to + noun/V-ing</b>. "
     "The <b>to</b> is a preposition, so it NEVER takes <i>to + V</i>.",
     ex("I <b>look forward to seeing</b> you. / <s>I look forward to see you</s> is WRONG.")),
    ("I'm interested ___ learning new skills.", "in", "interested in",
     "ERROR: <i>interested of / about</i>. Correct: <b>interested in</b>.",
     ex("I'm <b>interested in</b> learning new skills. / <s>I'm interested about</s> is WRONG.")),
    ("She gave me ___ helping hand.", "a", "a hand",
     "ERROR: 'give a hand' exists but does not mean 'lend a hand'. English: "
     "<b>give someone a hand</b> / <b>give someone a break</b>.",
     ex("<b>Give me a hand</b> with this. / <b>Give me a break</b> = give me a break.")),
    ("I'm going to ___ my driving licence.", "take", "take the test",
     "ERROR: 'get the licence'. In English: <b>take / get / pass</b> an exam. "
     "<b>Take</b> the exam, <b>pass</b> the exam, <b>fail</b> the exam.",
     ex("I'm going to <b>take</b> my driving test. / She <b>passed</b> the exam. / "
        "He <b>failed</b> it.")),
    ("Can you ___ me a favour?", "do", "do a favour",
     "ERROR: <i>make a favour</i>. In English: <b>do someone a favour</b>.",
     ex("Can you <b>do me a favour</b>? / <s>Make me a favour</s> is WRONG.")),
    ("We ___ at 9pm, so let's hurry.", "meet", "meet at 9",
     "ERROR: <b>meet</b> is not always 'arrange'. English: <b>meet</b> (to get "
     "together), <b>see</b> (to meet), <b>arrange to meet</b>.",
     ex("Let's <b>meet</b> at 9pm. / <b>See you later</b> / <b>Meet me there</b>.")),
    ("I'm ___ the dishes right now.", "doing", "do the dishes",
     "ERROR: 'wash'. In English, <b>do the dishes</b> is the standard expression.",
     ex("I'm <b>doing the dishes</b>. / <b>Do the washing-up</b> (BrE) / "
        "<b>do the dishes</b> (AmE).")),
    ("She's good ___ maths.", "at", "good at",
     "ERROR: <i>good in</i>. Correct: <b>good at</b> (skills) / <b>good with</b> "
     "(people).",
     ex("She's <b>good at</b> maths. / <s>She's good in maths</s> is WRONG.")),
    ("I usually go ___ bike to work.", "by", "by bike",
     "ERROR: <i>on bike</i>. Correct: <b>by bike</b> (+ <b>a</b> for a specific "
     "bike: <b>by a bike</b>).",
     ex("I go <b>by bike</b> to work. / I came <b>on foot</b>.")),
    ("He asked me ___ I could help.", "if/whether", "if/whether",
     "ERROR: 'he asked me that'. In English, indirect questions take <b>if / "
     "whether / that</b> and there is NO inversion of subject and verb.",
     ex("He asked me <b>if I could</b> help. / <s>He asked me if could I help</s> is WRONG.")),
    ("I'm going to ___ my grandparents.", "visit", "visit",
     "In English, <b>visit</b> + a person already means 'go and see'. "
     "<b>go to visit</b> = 'go to visit'.",
     ex("I'm going to <b>visit</b> my grandparents. / I'm <b>going to go to</b> the beach.")),
    ("There are a ___ of people at the party.", "lot", "a lot of",
     "ERROR: 'a lot of people of'. In English: <b>a lot of / lots of / plenty "
     "of</b> people.",
     ex("There are <b>a lot of</b> people at the party. / <b>Plenty of</b> / "
        "<b>tons of</b> / <b>loads of</b> people.")),
    ("I'll call you ___ I get home.", "as soon as", "as soon as",
     "ERROR: 'soon as' alone. English: <b>as soon as, as long as, as far as, "
     "as well as, as opposed to</b>.",
     ex("I'll call you <b>as soon as</b> I get home. / <b>As soon as</b> = as soon as.")),
    ("I agree ___ you.", "with", "agree with",
     "ERROR: 'agree with you' is right but students write <i>agree on you</i>. "
     "<b>agree with</b> + person, <b>agree on</b> + something, <b>agree to</b> + proposal.",
     ex("I <b>agree with</b> you. / We <b>agreed on</b> a price. / "
        "She <b>agreed to</b> meet at 8.")),
    ("It depends ___ the weather.", "on", "depend on",
     "ERROR: <i>depend of</i>. Correct: <b>depend on</b>.",
     ex("It <b>depends on</b> the weather. / <s>It depends of</s> is WRONG.")),
    ("She's very proud ___ her daughter.", "of", "proud of",
     "ERROR: <i>proud about her daughter</i> (acceptable but less natural). "
     "Correct: <b>proud of</b> (or <b>proud about</b>).",
     ex("She's <b>proud of</b> her daughter. / <b>Proud about</b> also works, "
        "but <b>of</b> is more natural.")),
    ("I need to ___ about the problem.", "sort", "sort out",
     "ERROR: 'repair'. For problems: <b>sort out, solve, deal with, tackle, "
     "address, resolve, get to grips with</b>.",
     ex("I need to <b>sort out</b> the problem. / <b>Solve</b> a problem / "
        "<b>deal with</b> a topic / <b>address</b> a problem.")),
    ("She's been working here ___ 2019.", "since", "since 2019",
     "ERROR: <i>for 2019</i>. English: <b>for</b> + duration, <b>since</b> + "
     "starting point.",
     ex("She's worked here <b>since 2019</b>. / <b>for</b> five years (duration).")),
], nivel="B1", tags=["l1-interference"])

# =================================================== CLASSIC B1 ERRORS

serie_gap(E2, [
    ("___ you like to go to the cinema?", "Do", "Do you like to go",
     "ERROR: <i>Do you like going...? Do you like going</i> when asking about an "
     "ACTIVITY. Correct: <b>Do you like going</b>? / <b>Do you like to go</b>? / "
     "<b>Do you enjoy going</b>? Use <b>to</b> when asking for an OPINION and "
     "<b>-ing</b> when asking about the ACTIVITY.",
     ex("<b>Do you like to go</b> to the cinema? (opinion) / "
        "<b>Do you like going</b> to the cinema? (activity).")),
    ("I ___ to London three times.", "have been", "have been",
     "ERROR: 'I went' for a past experience. In English, <b>have been</b> for "
     "experience with no time given; <b>went</b> if you give the time.",
     ex("I've <b>been to</b> London <b>three times</b>. / I <b>went to</b> London "
        "<b>in 2019</b> (with when → past).")),
    ("There ___ a lot of people at the concert.", "were", "there were",
     "ERROR: <i>there had</i>. In English: <b>there is / there are / there was / "
     "there were</b>. With the <b>Past Simple</b>: <b>there was / there were</b>.",
     ex("There <b>were</b> a lot of people at the concert. / <b>There is</b> / "
        "<b>There were</b> / <b>There will be</b>.")),
    ("He gave me ___ good advice.", "some", "some good advice",
     "ERROR: 'a good advice' / 'good advices'. <b>Advice</b> is UNCOUNTABLE: "
     "<b>some advice</b>, <b>a piece of advice</b>, <b>much advice</b>. NEVER "
     "<i>advices</i> or <i>an advice</i>.",
     ex("He gave me <b>some</b> good <b>advice</b>. / <b>a piece of advice</b> / "
        "<b>two pieces of advice</b> / <b>much advice</b>.")),
    ("She's taller ___ her brother.", "than", "taller than",
     "ERROR: 'more taller'. In English, <b>than</b> for comparatives and "
     "equality; <b>as...as</b> for 'as...as'.",
     ex("She's <b>taller than</b> her brother. / as <b>tall as</b> / not as "
        "<b>tall as</b>.")),
    ("I ___ to bed at 11 every night.", "go", "go to bed",
     "ERROR: 'sleep to bed'. In English, <b>go to bed</b> is reflexive. NEVER "
     "<i>sleep to bed</i>.",
     ex("I <b>go to bed</b> at 11. / <b>go to sleep</b> = to fall asleep.")),
    ("He's married ___ a doctor.", "to", "married to",
     "ERROR: <i>married with</i>. Correct: <b>married to</b>.",
     ex("He's <b>married to</b> a doctor. / <b>Engaged to</b>, <b>related to</b>.")),
    ("She suggested ___ a taxi.", "taking", "suggest taking",
     "ERROR: <i>suggested to take</i>. Correct: <b>suggest + V-ing</b> or "
     "<b>suggest + that + clause</b>.",
     ex("She <b>suggested taking</b> a taxi. / "
        "<b>suggested that we (should) take</b> a taxi.")),
    ("If it ___ tomorrow, we'll stay home.", "rains", "if it rains",
     "ERROR: 'if it will rain'. In English, <b>if + present simple</b> for "
     "hypotheses: <b>if it rains</b>.",
     ex("<b>If</b> it <b>rains</b> tomorrow, we'll stay home. / "
        "<s>If it will rain</s> is WRONG. / <s>If it would rain</s> is WRONG.")),
    ("He's been living here ___ 5 years.", "for", "for 5 years",
     "ERROR: 'for 5 years' is right, but students write <i>since 5 years</i>. "
     "In English, <b>for</b> + duration.",
     ex("He's been living here <b>for</b> 5 years. / <b>for</b> 5 years "
        "(duration) / <b>since</b> 2019 (point).")),
    ("I ___ you tomorrow.", "will call", "will call",
     "ERROR: 'will you call'. In English, <b>will</b> goes BEFORE the verb.",
     ex("I <b>will call</b> you tomorrow. / <s>I will you call</s> is WRONG. / "
        "<s>I call you tomorrow</s> is WRONG.")),
    ("The more you practise, ___ you get.", "the better", "the better",
     "ERROR: 'the more better'. In English: <b>The + comparative, the + "
     "comparative</b>.",
     ex("The more you practise, <b>the better</b> you get. / <b>The more</b>…, "
        "<b>the more</b>… / <b>The less</b>…, <b>the less</b>… / "
        "<s>more better</s> is WRONG.")),
], nivel="B1", tags=["error b1"])

# ===================================================== B2-C1 ERRORS

serie_gap(E3, [
    ("If I ___ you, I'd take the job.", "were", "if I were you",
     "ERROR: 'if I would be you'. In English, <b>if + were</b> for unreal "
     "hypotheses, with all persons.",
     ex("<b>If I were</b> you, I'd take the job. / <s>If I was you</s> "
        "(AmE informal) / <s>If I would be you</s> is WRONG.")),
    ("I suggest you ___ a doctor.", "see", "suggest you see",
     "ERROR: <i>suggest you to see</i>. Suggestion verbs (<b>suggest, recommend, "
     "advise, propose, insist</b>) take <b>that + clause</b> or <b>+ V-ing</b>.",
     ex("I <b>suggest you see</b> a doctor. / <s>I suggest you to see</s> is WRONG.")),
    ("The meeting was ___ by the boss.", "postponed", "was postponed",
     "ERROR: a wrong passive. In English: <b>postpone</b> = <b>be postponed</b> "
     "/ <b>be put off</b>.",
     ex("The meeting was <b>postponed by</b> the boss. / <b>postpone</b> = "
        "postpone / <b>delay</b> = delay / <b>prolong</b> = prolong.")),
    ("She's good ___ playing the piano.", "at", "good at playing",
     "ERROR: 'be good at + V'. English: <b>good at + V-ing</b> or <b>good at + "
     "noun</b>.",
     ex("She's <b>good at playing</b> the piano. / <b>good with</b> (people) / "
        "<b>good at</b> (skills).")),
    ("He denied ___ the money.", "stealing", "denied stealing",
     "ERROR: 'denied to steal'. Correct: <b>deny + V-ing</b> (past) or "
     "<b>deny + to + base</b> (future).",
     ex("He <b>denied stealing</b> the money. / He <b>denied taking</b> it. / "
        "She <b>denied to take</b> it (future).")),
    ("She apologised ___ breaking the vase.", "for", "apologised for",
     "ERROR: <b>apologise to breaking</b>. Correct: <b>apologise for + "
     "V-ing</b>.",
     ex("She <b>apologised for breaking</b> the vase. / <b>apologise to</b> + "
        "person / <b>apologise for</b> + thing.")),
    ("I need to ___ about the exam results.", "find out", "find out about",
     "ERROR: 'know about'. For 'to find out': <b>find out, hear about, learn "
     "about, be told, come to know</b>.",
     ex("I need to <b>find out about</b> the results. / <b>find out</b> = find "
        "out / <b>find about</b> is WRONG.")),
    ("I'm looking forward ___ you.", "to seeing", "to seeing",
     "ERROR: <i>look forward to see you</i>. The <b>to</b> is a preposition, so "
     "it goes with <b>-ing</b>.",
     ex("I'm looking forward <b>to seeing</b> you. / <b>look forward to</b> + "
        "<b>noun</b> or <b>V-ing</b>, never <i>to + V</i>.")),
    ("The book ___ by a famous writer.", "was written", "was written",
     "ERROR: a badly formed passive. Always <b>be + participle</b>.",
     ex("The book <b>was written by</b> a famous writer. / <b>has been written</b> / "
        "<b>will be written</b>.")),
    ("I'd rather you ___ smoke in front of me.", "didn't",
     "would rather you didn't",
     "ERROR: <i>would rather you not to smoke</i>. <b>Would rather + subject + "
     "Past Simple</b> for someone else's past; <b>would rather not + base</b> "
     "for yourself.",
     ex("I'd <b>rather you didn't smoke</b> in front of me. / "
        "<b>would rather + base</b> (own) / <b>would rather + past</b> (other).")),
    ("He arrived ___ the airport two hours late.", "at", "arrive at",
     "ERROR: <i>arrive in</i> for everywhere. English: <b>arrive in</b> + "
     "city/country, <b>arrive at</b> + small place. With <b>at the airport / at "
     "the station</b>.",
     ex("He arrived <b>at</b> the airport two hours late. / <b>arrive in</b> + "
        "city / <b>arrive at</b> + small place.")),
    ("___ the fact that he was tired, he kept working.", "Despite",
     "despite the fact that",
     "ERROR: 'despite that'. <b>Despite</b> + <b>-ing/noun</b>; <b>although / "
     "even though</b> + clause.",
     ex("<b>Despite the fact that</b> he was tired, he kept working. / "
        "<b>Although</b> he was tired, he kept working.")),
    ("She has a ___ for languages.", "knack", "a knack for",
     "ERROR: 'a don for'. English: <b>knack for, flair for, talent for, head "
     "for, gift for</b>.",
     ex("She has a <b>knack for languages</b>. / <b>a gift for</b> / "
        "<b>a flair for</b> / <b>a talent for</b>.")),
    ("I haven't seen him ___ 2019.", "since", "since 2019",
     "ERROR: 'for 2019'. With <b>haven't seen</b> use <b>since</b> (a point) or "
     "<b>for</b> (a duration).",
     ex("I haven't seen him <b>since 2019</b>. / <b>for</b> five years. NEVER "
        "<i>since five years</i>.")),
], nivel="B2", tags=["error b2 c1"])

# ============================================ SPELLING AND PRONUNCIATION

gap(E4, "I haven't seen him ___ a long time.", "for", nivel="B1",
    cue="for a long time", forma="for",
    regla="Fixed: <b>for a long time, for ages, for good, for ever (or "
          "<b>forever</b>), for now, for example, for instance</b>.",
    ejemplos=ex("I haven't seen him <b>for</b> a long time.",
                "<b>for ever</b> / <b>forever</b> = forever."),
    notas="<b>for ever</b> (two words) and <b>forever</b> (one) both mean "
          "'forever', but they are used in different contexts: "
          "<i>live <b>forever</b></i> / <i>wait <b>for ever</b></i>.",
    tags="fixed-phrase for")

gap(E4, "She's ___ my best friend.", "one of", nivel="B1", cue="one of",
    regla="<b>one of + the + plural</b> = one of. <b>One of my best friends</b>.",
    ejemplos=ex("She's <b>one of</b> my best friends.",
               "He's <b>one of the</b> best players."),
    notas="<b>One of</b> is always followed by a plural. And the verb is "
          "singular: <i>She's <b>one of the</b> best <b>players</b> in the "
          "world.</i>",
    tags="one-of")

gap(E4, "I need to buy ___ groceries.", "some", nivel="B1",
    cue="some groceries",
    regla="<b>Some</b> as a plural noun: <b>some groceries, some clothes, some "
          "trousers, some glasses, some scissors, some belongings, some "
          "customs, some funds, some premises, some supplies</b>.",
    ejemplos=ex("I need to buy <b>some groceries</b>.",
                "<b>some clothes</b> / <b>some trousers</b> / <b>some scissors</b>"),
    notas="Plural-only nouns: <b>clothes, trousers, jeans, glasses, scissors, "
          "pyjamas, briefs, goods, belongings, customs, funds, premises, "
          "supplies, surroundings, athletics, mumps, measles, rabies</b>.",
    tags="plural-uncountable")

gap(E4, "The police are investigating ___ . It's a serious crime.", "it",
    nivel="B2", cue="it", forma="It",
    regla="<b>It</b> refers to a whole situation, not to an object. "
          "<b>They</b> refers to several objects.",
    ejemplos=ex("The police are investigating. <b>It</b> is a serious crime.",
               "The houses are empty. <b>They</b> were sold last year."),
    notas="<b>It</b> = the case / the situation. <b>They</b> = the things. This "
          "distinction does not exist in many languages.",
    tags="it they reference")

tabla(E4, ["Word", "Pronunciation", "Trap"],
     [["thirteen / thirty", "/θɜːˈtiːn/ / /ˈθɜːti/", "<b>TH</b>, not <b>DR</b>"],
      ["thought", "/θɔːt/", "<b>TH</b> + <b>ough</b> = 'ot'"],
      ["through / thorough", "/θruː/", "<b>TH</b> + <b>ough</b> = 'ru'"],
      ["though / although", "/ðəʊ/", "no <b>f</b>"],
      ["would / could / should", "/wʊd/", "no <b>ll</b>"],
      ["sword / world / word", "/sɔːd, wɜːld, wɜːd/", "no <b>v</b>"],
      ["laugh / daughter / eight", "/lɑːf/", "silent <b>gh</b>"],
      ["island", "/ˈaɪlənd/", "the <b>s</b> is silent"],
      ["half / calf / walk", "/hɑːf, kɑːf, wɔːk/", "silent <b>l</b>"],
      ["listen / often / fasten", "/ˈlɪsn, ˈɒfn, ˈfɑːsn/", "silent <b>t</b>"],
      ["answer", "/ˈɑːnsə/", "silent <b>w</b>"],
      ["hour / honest / honour", "/ˈaʊə, ˈɒnɪst, ˈɒnə/", "silent <b>h</b>"],
      ["wednesday", "/ˈwenzdɪ/", "spelled with <b>d</b>, not <b>t</b>"],
      ["receive / ceiling", "/rɪˈsiːv, ˈsiːlɪŋ/", "<b>ei</b> = /iː/"],
      ["business", "/ˈbɪznəs/", "silent <b>u</b>. <b>business</b> ≠ <b>bizness</b>"],
      ["cache / chaos", "/kæʃ, keɪɒs/", "<b>ch</b> = /ʃ/ vs <b>ch</b> = /k/"],
      ["genre / genuine", "/ˈʒɒnrə, ˈdʒenjuɪn/", "<b>gen</b> = /ʒ/ or /dʒ/"]],
     titulo="Pronunciation traps that make the difference in an oral exam",
     nivel="C1",
     nota="If you take an <b>IELTS/TOEFL</b> speaking test, <b>th</b>, final "
          "<b>-ed</b> and long vowels are what cost you the most marks.")

cloze(E1, "I look forward to {{c1::seeing}} you.",
      extra="<div class='box warn'><span class='lbl'>Error #1 for L1 speakers</span>"
            "<b>to</b> is a PREPOSITION → always <b>-ing</b>. "
            "<i>to see</i> is an error in any exam.</div>",
      tags="c1-c2 error cloze")
