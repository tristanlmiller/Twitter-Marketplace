# Twitter Ads Marketplace

This is a take-home assignment for a job application.  The data and assignment are excluded from this repository, and it is not intended to be understood by broad audiences.

Currently a work in progress.

# Spending and Engagement rates

We begin by looking at how much each campaign has spent over time, shown below.

<div align="center"><img src="Images/spend vs time.png" alt="Spend vs time"></div>

And here is a table of information about each campaign:

 	budget 	total spent 	bid 	objective 	targeting 	engagement 	ECPI
1 	500.00 	499.412728 	7.50 	WEBSITE_CLICKS 	GEO 	0.038462 	0.288462
2 	3550.00 	1210.169699 	1.15 	WEBSITE_CLICKS 	NaN 	0.007496 	0.008621
3 	1000.00 	61.002298 	1.50 	APP_INSTALLS 	['LANGUAGE', 'GEO'] 	0.025210 	0.037815
4 	1167.00 	115.240681 	1.00 	APP_INSTALLS 	['GEO', 'GENDER'] 	0.003472 	0.003472
5 	170.00 	169.471740 	0.50 	VIDEO_VIEWS 	['AGE_BUCKET', 'GEO'] 	0.338462 	0.169231
6 	138.89 	138.453629 	0.05 	VIDEO_VIEWS 	['AGE_BUCKET', 'GEO'] 	0.219436 	0.010972
7 	1075.00 	1073.198580 	0.50 	VIDEO_VIEWS 	['GEO'] 	0.348185 	0.174092

Campaign 1 is the fastest spender on the list, but stops after a few hours because it has reached its maximum budget.  By comparison, campaign 2 spends more slowly, and never reaches its max.  If we look at the campaign parameters, this makes sense.  Campaign 1 has a much higher bid and lower maximum budget, as well as higher engagement rate.  They're going to win a lot of auctions that way.

If I were to give advice to Campaigns 1 and 2, this is what I'd say:

Campaign 1 appears to be overbidding, or underbudgeting, unless they particularly care about getting lots of attention within a 3 hour window.  Although it's a second price auction, which in theory incentivizes clients to be honest about how much they value their objective, it seems they could benefit from strategically lowering their bid, getting more clicks for their dollar.

Campaign 2 seems to be underbidding.  I would gently suggest that they bid higher, although maybe they have a good reason not to.  Oddly, despite campaign 2 having lower ECPI than most of the other campaigns, they still manage to win a lot of auctions, which may have to do with the fact that they didn't select any target geographical region.  Maybe they're winning a bunch of auctions in third world countries, where advertising isn't competitive!  Campaign 2 should consider whether they're happy with the audience they're getting.

Other thoughts on the curves:

- Campaign 2 seems to spend less around hour 20 (3 am UTC).  From this, I would guess that they're getting ads served to western Europe?  Maybe that's the least competitive market?

- It is strange to me that Campaign 1 has a logistic shape instead of being more linear.  Is it due to variation throughout the day?  Or does Twitter dynamically lower their bid as they approach their maximum budget?  And does the acceleration at the beginning indicate Twitter's algorithm becoming more optimistic about the campaign over time?