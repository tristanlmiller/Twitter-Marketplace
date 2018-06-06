# Twitter Ads Marketplace

This is a take-home assignment for a job application.  The data and assignment are excluded from this repository, and it is not intended to be understood by broad audiences.

Currently a work in progress.

# Spending and Engagement rates

We begin by looking at how much each campaign has spent over time, shown below.

<div align="center"><img src="Images/spend vs time.png" alt="Spend vs time"></div>

And here is a table of information about each campaign:

<div align="center"><img src="Images/campaign info.png" alt="Campaign info"></div>

Campaign 1 is the fastest spender on the list, but stops after a few hours because it has reached its maximum budget.  By comparison, campaign 2 spends more slowly, and never reaches its max.  If we look at the campaign parameters, this makes sense.  Campaign 1 has a much higher bid and lower maximum budget, as well as higher engagement rate.  They're going to win a lot of auctions that way.

If I were to give advice to Campaigns 1 and 2, this is what I'd say:

**Campaign 1** appears to be overbidding, or underbudgeting, unless they particularly care about getting lots of attention within a 3 hour window.  Although it's a second price auction, which in theory incentivizes clients to be honest about how much they value their objective, it seems they could benefit from strategically lowering their bid, getting more clicks for their dollar.

**Campaign 2** seems to be underbidding.  I would gently suggest that they bid higher, although maybe they have a good reason not to.  Oddly, despite campaign 2 having lower ECPI than most of the other campaigns, they still manage to win a lot of auctions, which may have to do with the fact that they didn't select any target geographical region.  Maybe they're winning a bunch of auctions in third world countries, where advertising isn't competitive!  Campaign 2 should consider whether they're happy with the audience they're getting.

Other thoughts on the curves:

- Campaign 2 seems to spend less around hour 20 (3 am UTC).  From this, I would guess that they're getting ads served to western Europe?  Maybe that's the least competitive market?

- It is strange to me that Campaign 1 has a logistic shape instead of being more linear.  Is it due to variation throughout the day?  Or does Twitter dynamically lower their bid as they approach their maximum budget?  And does the acceleration at the beginning indicate Twitter's algorithm becoming more optimistic about the campaign over time?