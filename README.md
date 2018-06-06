# Twitter Ads Marketplace

This is a take-home assignment for a job application.  The data and assignment are excluded from this repository, and it is not intended to be understood by broad audiences.

Currently a work in progress.

# Spending and Engagement rates

We begin by looking at how much each campaign has spent over time, shown below.

<div align="center"><img src="Images/spend vs time.png" alt="Spend vs time"></div>

And here is a table of information about each campaign:

<div align="center"><img src="Images/campaign info.png" alt="Campaign info"></div>

'ads seen' refers to the probability the ad will be seen, conditional on it being served.  'ECPI' refers to the expected revenue conditional on the ad being served and seen.

Campaign 1 is the fastest spender on the list, but stops after a few hours because it has reached its maximum budget.  By comparison, campaign 2 spends more slowly, and never reaches its max.  If we look at the campaign parameters, this makes sense.  Campaign 1 has a much higher bid and lower maximum budget, as well as higher engagement rate.  They're going to win a lot of auctions that way.

If I were to give advice to Campaigns 1 and 2, this is what I'd say:

**Campaign 1** appears to be overbidding, or underbudgeting, unless they particularly care about getting lots of attention within a 3 hour window.  Although it's a second price auction, which in theory incentivizes clients to be honest about how much they value their objective, it seems they could benefit from strategically lowering their bid, getting more clicks for their dollar.

**Campaign 2** seems to be underbidding.  I would gently suggest that they bid higher, although maybe they have a good reason not to.  Oddly, despite campaign 2 having lower ECPI than most of the other campaigns, they still manage to win a lot of auctions, which may have to do with the fact that they didn't select any target geographical region.  Maybe they're winning a bunch of auctions in third world countries, where advertising isn't competitive!  Campaign 2 should consider whether they're happy with the audience they're getting.

Other thoughts on the curves:

- Campaign 2 seems to spend less around hour 20 (3 am UTC).  From this, I would guess that they're getting ads served to western Europe or Africa?  Maybe that's the least competitive market?

- It is strange to me that Campaign 1 has a logistic shape instead of being more linear.  Is it due to variation throughout the day?  Or does Twitter dynamically lower their bid as they approach their maximum budget?  And does the acceleration at the beginning indicate Twitter's algorithm becoming more optimistic about the campaign over time?

# Discussion of campaign pacing

**Objectives** - Campaigns that seek to get video views have a much higher engagement rate than the others, by about a factor of 10.  Accordingly, their bid is about 10 times smaller, so they can compete in the same market.

**Pacing** - Most campaigns seem to spend almost all their budget, or very little of it.  There is likely some tipping point where their bid is high enough that they start winning a large number of auctions.

**ECPI** - Campaigns with a higher ECPI seem to be more successful, but it isn't completely determinative.  Well, maybe Campaign 3 simply hasn't been charged much because it started late in the day.  Come to think of it, this isn't the real ECPI, because we're only looking at data from auctions they actually won.  That's a hell of a selection bias.

**Targeting** - I don't really expect pacing to be related to targeting.  For example, if you were to look at men and women, either men are the more competitive market, or women are, and if a client wants to target a particular gender, I wouldn't know if they're participating in a more or less competitive market without knowing *which* gender they're targeting.  Granted, clients probably are most likely to go to the more crowded market, that's why it's crowded.

**Ads seen** - For some reason, a greater percentage of ads targeting video views or website clicks actually get seen by the user.  This is a bit strange, and maybe there's something about the mechanics of "seeing" ads that I'm missing.  On the other hand, maybe Twitter's algorithm simply finds that app downloads are relatively more successful among Twitter users who scroll down a lot.  So apps are more likely to win auctions that are further down the feed.

# My experience with this project

It's fun to explore the data in this way.  Some of my observations suggest potentially interesting trends (e.g. are apps more successful among heavy Twitter users?), and others suggest potentially useful actions (e.g. should Twitter advise people to decrease their bids, or does that go against Twitter's interests?).

I was a little confused at first about the definition of "engagement rate".  Since I was just looking at the spend rate (over time!) I thought engagement rate was also over time, and I already made several plots before I realized that must be wrong.  Making plots that look nice is easily the most time-consuming aspect.