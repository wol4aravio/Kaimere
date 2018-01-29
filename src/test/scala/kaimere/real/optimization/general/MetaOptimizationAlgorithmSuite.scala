package kaimere.real.optimization.general

import kaimere.real.optimization._
import kaimere.real.optimization.classic.zero_order.RandomSearch
import kaimere.real.optimization.general.Instruction.MaxTime
import org.scalatest.FunSuite
import spray.json._

class MetaOptimizationAlgorithmSuite extends FunSuite {

  private val epsNorm = 1e-2
  private val maxTries = 10
  private val maxTime = 0.5

  private val rs: OptimizationAlgorithm = RandomSearch(10, 0.01)
  private val SA: OptimizationAlgorithm = MetaOptimizationAlgorithm(
    algorithms = Seq(rs, rs, rs),
    instructions = Seq(MaxTime(maxTime), MaxTime(maxTime), MaxTime(maxTime)),
    targetVars = Seq(Some(Set("x", "a")), Some(Set("y", "b")), Some(Set("z", "c")))
  )

  test("Dummy #4 (by max time)") {

    val passed = Tester(
      tool = SA,
      f = DummyFunctions.func_4,
      area = DummyFunctions.area_4,
      state = None,
      instruction = null,
      epsNorm = epsNorm,
      maxTries = maxTries)

    assert(passed)

  }

}
