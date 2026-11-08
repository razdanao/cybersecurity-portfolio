# Canadian Cyber Law and International Frameworks

Status: **Final**

Reference notes on three frameworks that come up repeatedly when discussing privacy, fraud, and cybercrime law in a Canadian context — useful background for the legal/regulatory sections of the [Marriott/Starwood case study](../case-studies/marriott-starwood-breach-2018.md) and similar material.

## CASL (Canada's Anti-Spam Legislation)
CASL prohibits sending a commercial electronic message (CEM) without the recipient's consent, aiming to reduce the volume of spam Canadians receive. A message counts as a CEM when encouraging participation in a commercial activity is its primary purpose, or one of its purposes — the commercial character can come from the message's content, a link to a commercial site, or even a company logo unrelated to the sender.

Key requirements:
- **Consent** (express or implied) is required before sending a CEM — notably, even a request *for* consent is itself treated as a CEM.
- Every CEM must **identify the sender** and the **purpose of the message**.
- Every CEM must give recipients an **easy way to opt out** of future messages.
- Non-compliance carries significant administrative monetary penalties — up to $1 million per violation for an individual and $10 million per violation for an organization.

CASL is enforced jointly by the CRTC, the Competition Bureau, and the Office of the Privacy Commissioner of Canada, reflecting its overlap with both anti-spam and privacy concerns.

## CAFC (Canadian Anti-Fraud Centre)
Canada's national anti-fraud call centre and central fraud data repository, formerly known as PhoneBusters. Its original mandate focused on prosecuting telemarketing fraud in Ontario and Quebec under the Criminal Code; its scope has since broadened considerably to cover mass-marketing fraud, identity theft, deceptive marketing practices, and telemarketing fraud more generally.

What it does:
- Collects intelligence and receives complaints on fraud from the public.
- Runs public education and awareness campaigns (notably during March, Fraud Prevention Month) to reduce future victimization.
- Helps individuals and businesses report fraud, learn to recognize warning signs, and understand how to protect themselves.
- Shares intelligence with law enforcement and government partners in Canada and internationally, supporting efforts to disrupt fraud networks and strengthen public-private cooperation on financial crime.

## Budapest Convention (Convention on Cybercrime)
The first international treaty addressing crimes committed via the internet and other computer networks, covering offenses including copyright infringement, computer-related fraud, child exploitation material, and violations of network security. Beyond defining offenses, it establishes procedural powers (such as the search of computer networks and lawful interception) needed to actually investigate them.

Its stated objective is to pursue a common criminal policy to protect society from cybercrime, principally by:
- **Harmonizing** domestic criminal law definitions and related provisions across signatory states for cybercrime offenses.
- **Establishing domestic procedural powers** needed to investigate and prosecute cyber offenses, including offenses where evidence exists in electronic form.
- **Setting up a framework for fast, effective international cooperation**, since cybercrime routinely crosses jurisdictional boundaries in a way traditional crime doesn't.

Specific offenses it defines include: illegal access, illegal interception, data interference, system interference, misuse of devices, computer-related forgery, computer-related fraud, offenses related to child exploitation material, and offenses related to copyright and related rights.

**Why this matters for incident response specifically:** when a breach (like Marriott/Starwood) spans victims in multiple countries, frameworks like the Budapest Convention are part of what makes cross-border evidence-sharing and law enforcement cooperation possible at all — without some harmonized baseline, an investigator in one country has no reliable mechanism to request assistance or evidence from another.
