Assignment: make class Linear Regression, make class KNN.

Difference
LR:
+ can extrapolate
- can be very complex depending on tuples
equation-based. data in -> apply to eqn -> out
KNN:
+ can fit easily
- cannot extrapolate (edges, averaged will give flatline since nearest neighbors are the N-outermost for a while)
uses actual data. new data -> compare to old -> result averaged output of N-nearest inputs

==================================

To measure performance,
    looking at error: RMS of TEST DATA not training!
        train: 60%
        test: 40%
        in case not enough data, can use cross-validation.
        example: split into 5, 5 iterations:
        train using 1-4, test using 5.
        train using 2-5, test using 1.
        train using 1,3-5, test using 2.
        train using 1-2,4-5, test using 3.
        train using 1-3,5, test using 4.
        So we have 5 tests.

        But this usually isn't fit for fins data since it uses future data. This makes the model too good, it's a hax.
        Use roll forward cross validation. Same thing, with one additional caveat:
        TEST DATA MUST BE MOST RECENT, DO NOT USE FOR TRAINING

    plot error:
        plot y predicted vs. actual y and see if they correlate. np.corrcoef()
        range [-1       0            1]
              [inverse  no  correlated]

correlation and RMS don't go hand in hand. this is especially so if there's a large bias.

==================================

Much ado about Overfitting

Linear regression:
Test -> error decreases with iterations till lim.
Training -> error decreases, though still higher than test, then shots back up at certain point.

This would be the region of overfitting.

KNN:
the smaller the K, the more fitted. but test would have a high error almost always due to this.
as K gets bigger, it becomes more generalized - thus test error goes down, but too general and it goes back up.

==================================

ENSEMBLE LEARNERS

If one just won't cut it, try adding more!
It's like a portfolio of learners. Portfolioception!

Usually:
- lower error
- less overfitting
b/c indiv bias gets diluted either by averaging or going against eachother.

To build:
a. Train several parametrized polynomials of differing degree
b. Train several KNN models using different subsets of data
c. Combine a and b.

Another way to build:
bootstrap aggregating
bagging
a. create subsets of training data. random with replacement - members are picked randomly, duplicates fine.
   subsets contain <= 60% of original training data
b. train each, get models, collect outputs and mean them.

boosting: specialized bagging
Ada(ptive) boost:
a. make bags, train first bag.
b. train second bag, but the training data with more errors in the first bag iteration gets more weight (more likely to be chosen).
c. iterate as usual till last bag, combine outputs

Yes, this makes adaboost more prone to overfitting.

Boosting and bagging are meta-algorithms that wrap the existing methods.
- reduces error
- reduces overfitting

==================================

REINFORCEMENT LEARNING

here we have a closed feedback loop.
S = input from environment
r = reward
a = action (output).
Takes in S - what is happening?
Measure according to a rule the value - rewarding or not?
Then outputs an action which affects the environment. Then the loop begins anew.
Example:        s   a   r
Buy                 v
Sell                v
Long posn       v
Bollinger       v
Trade return            v
Daily return    v       v

A more formal defn would be a Markov decision problems statement.
RL algos solve MDPs!
+ Set of states S
+ Set of actions A
+ Transition function T[s, a, s']
    telling the probability that based on states s, action a will produce new state s'.
+ Reward function R[a, s]
Find policy pi(s) that will maximize reward.

T policy iteration,
R value iteration,
but so far they haven't been explained in this course.

Policy-building can be done in these ways:
Model-based
    Build a model of                <s1 a1 s1' r1>
        T[s, a, s']                 <s2 a2 s2' r2>
        R[s, a]                           ...
        Value/policy iteration            ...
    Essentially building experience tuples.
Model-free
    Q-learning

Now to put in some contraints to help further define the problem.
What to optimize?
infinite horizon: sum of all, find largest.
finite horizon: constrained x-steps/time/period, find largest (can also be thought of as local max)
In fins is esp important since there is the time value of money. This manifests in the form of
---discounted reward---
