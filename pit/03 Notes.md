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


