﻿using System;
using System.Collections.Generic;
using System.Linq;

namespace OSOL.Extremum.Core.DotNet.Random.Distributions
{
    public interface IDiscreteUniform
    {
        int GetDiscreteUniform(int min, int max);   
    }

    public static class DiscreteUniformFunctions
    {
        public static Dictionary<string, int> Diameter(this IDiscreteUniform GoRN, Dictionary<string, Tuple<int, int>> area) =>
            area.ToDictionary(kvp => kvp.Key,
                kvp => GoRN.GetDiscreteUniform(kvp.Value.Item1, kvp.Value.Item2));
    }

}