﻿using System;
using Xunit;

using OSOL.Extremum.Core.DotNet.Arithmetics;

namespace OSOL.Extremum.Core.DotNet.Tests
{
    public class IntervalTests
    {
        Interval i1 = new Interval(-1.0, 2.0);
        Interval i2 = new Interval(-4.0, 3.0);
        Interval i3 = new Interval(1.0, 2.0);
        Interval i4 = new Interval(5.0, 5.1);
        Interval i5 = new Interval(-6.0, -5.0);
        Interval i6 = new Interval(-2.0, 0.0);
        Interval i7 = new Interval(0.0, 3.0);

        [Fact]
        void TestToString()
        {
            Assert.True(i1.ToString().Equals("[-1; 2]"));
            Assert.True(i4.ToString().Equals("[5; 5.1]"));
            Assert.True(i7.ToString().Equals("[0; 3]"));
        }

        [Fact]
        void TestMiddlePoint()
        {
            Assert.Equal(i1.MiddlePoint, 0.5);
            Assert.Equal(i3.MiddlePoint, 1.5);
            Assert.Equal(i7.MiddlePoint, 1.5);
        }

        [Fact]
        void TestWidth()
        {
            Assert.Equal(i1.Width, 3.0);
            Assert.Equal(i3.Width, 1.0);
            Assert.Equal(i7.Width, 3.0);
        }

        [Fact]
        void TestRadius()
        {
            Assert.Equal(i1.Radius, 1.5);
            Assert.Equal(i3.Radius, 0.5);
            Assert.Equal(i7.Radius, 1.5);
        }

        [Fact]
        void TestApproximateEquality()
        {
            Assert.True(i1.ApproximatelyEqualsTo(i1 + 1e-7));
            Assert.False((new Interval(double.NegativeInfinity, 0.0)).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, double.NaN)));
        }

        [Fact]
        void TestAddition()
        {
            Assert.True((i1 + i2).ApproximatelyEqualsTo(new Interval(-5.0, 5.0)));
            Assert.True((i2 + i3).ApproximatelyEqualsTo(new Interval(-3.0, 5.0)));
            Assert.True((i5 + i4).ApproximatelyEqualsTo(new Interval(-1.0, 0.1)));
        }

        [Fact]
        void TestSubtraction()
        {
            Assert.True((i1 - i2).ApproximatelyEqualsTo(new Interval(-4.0, 6.0)));
            Assert.True((i2 - i3).ApproximatelyEqualsTo(new Interval(-6.0, 2.0)));
            Assert.True((i5 - i4).ApproximatelyEqualsTo(new Interval(-11.1, -10.0)));
        }
        
        [Fact]
        void TestMultiplication()
        {
            Assert.True((i1 * i2).ApproximatelyEqualsTo(new Interval(-8.0, 6.0)));
            Assert.True((i2 * i3).ApproximatelyEqualsTo(new Interval(-8.0, 6.0)));
            Assert.True((i5 * i4).ApproximatelyEqualsTo(new Interval(-30.6, -25.0)));
        }
        
        [Fact]
        void TestDivision()
        {
            Assert.True((i1 / i2).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, double.PositiveInfinity)));
            Assert.True((i2 / i3).ApproximatelyEqualsTo(new Interval(-4.0, 3.0)));
            Assert.True((i1 / i5).ApproximatelyEqualsTo(new Interval(-0.4, 0.2)));
            Assert.True((i3 / i6).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, -0.5)));
            Assert.True((i5 / i7).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, -5.0 / 3.0)));
        }
        
        [Fact]
        void TestPower()
        {
            Assert.True((i1.Power(2.0)).ApproximatelyEqualsTo(new Interval(0.0, 4.0)));
            Assert.True((i2.Power(3.0)).ApproximatelyEqualsTo(new Interval(-64.0, 27.0)));
            Assert.True((i5.Power(0.0)).ApproximatelyEqualsTo(new Interval(1.0, 1.0)));
        }

        [Fact]
        void TestNeg()
        {
            Assert.True((-i1).ApproximatelyEqualsTo(new Interval(-2.0, 1.0)));
            Assert.True((-i5).ApproximatelyEqualsTo(new Interval(5.0, 6.0)));
            Assert.True((-i6).ApproximatelyEqualsTo(new Interval(0.0, 2.0)));
        }

        [Fact]
        void TestSin()
        {
            Assert.True((i1.Sin()).ApproximatelyEqualsTo(new Interval(Math.Sin(-1.0), 1.0)));
            Assert.True((i2.Sin()).ApproximatelyEqualsTo(new Interval(-1.0, 1.0)));
            Assert.True((i3.Sin()).ApproximatelyEqualsTo(new Interval(Math.Sin(1.0), 1.0)));
            Assert.True((i6.Sin()).ApproximatelyEqualsTo(new Interval(-1.0, 0.0)));
        }

        [Fact]
        void TestCos()
        {
            Assert.True((i1.Cos()).ApproximatelyEqualsTo(new Interval(Math.Cos(2.0), 1.0)));
            Assert.True((i2.Cos()).ApproximatelyEqualsTo(new Interval(-1.0, 1.0)));
            Assert.True((i3.Cos()).ApproximatelyEqualsTo(new Interval(Math.Cos(2.0), Math.Cos(1.0))));
            Assert.True((i6.Cos()).ApproximatelyEqualsTo(new Interval(Math.Cos(-2.0), 1.0)));
        }

        [Fact]
        void TestAbs()
        {
            Assert.True((i1.Abs()).ApproximatelyEqualsTo(new Interval(0.0, 2.0)));
            Assert.True((i2.Abs()).ApproximatelyEqualsTo(new Interval(0.0, 4.0)));
            Assert.True((i3.Abs()).ApproximatelyEqualsTo(new Interval(1.0, 2.0)));
            Assert.True((i4.Abs()).ApproximatelyEqualsTo(new Interval(5.0, 5.1)));
            Assert.True((i5.Abs()).ApproximatelyEqualsTo(new Interval(5.0, 6.0)));
            Assert.True((i6.Abs()).ApproximatelyEqualsTo(new Interval(0.0, 2.0)));
            Assert.True((i7.Abs()).ApproximatelyEqualsTo(new Interval(0.0, 3.0)));
        }
        
        [Fact]
        void TestExp()
        {
            Assert.True((i1.Exp()).ApproximatelyEqualsTo(new Interval(Math.Exp(-1.0), Math.Exp(2.0))));
            Assert.True((i2.Exp()).ApproximatelyEqualsTo(new Interval(Math.Exp(-4.0), Math.Exp(3.0))));
            Assert.True((i3.Exp()).ApproximatelyEqualsTo(new Interval(Math.Exp(1.0), Math.Exp(2.0))));
        }

        [Fact]
        void TestSqrt()
        {
            Assert.True(i1.Sqrt().ApproximatelyEqualsTo(new Interval(0.0, Math.Sqrt(2.0))));
            Assert.True(i3.Sqrt().ApproximatelyEqualsTo(new Interval(Math.Sqrt(1.0), Math.Sqrt(2.0))));
            Assert.Throws<IntervalExceptions.BadAreaOperationException>(() => i5.Sqrt());
        }
        
        [Fact]
        void TestLn()
        {
            Assert.True((i1.Ln()).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, Math.Log(2.0))));
            Assert.True((i2.Ln()).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, Math.Log(3.0))));
            Assert.True((i3.Ln()).ApproximatelyEqualsTo(new Interval(Math.Log(1.0), Math.Log(2.0))));
            Assert.True((i4.Ln()).ApproximatelyEqualsTo(new Interval(Math.Log(5.0), Math.Log(5.1))));
            Assert.Throws<IntervalExceptions.BadAreaOperationException>(() => i5.Ln());
            Assert.True((i6.Ln()).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, double.NegativeInfinity)));
            Assert.True((i7.Ln()).ApproximatelyEqualsTo(new Interval(double.NegativeInfinity, Math.Log(3.0))));
        }
    }
}