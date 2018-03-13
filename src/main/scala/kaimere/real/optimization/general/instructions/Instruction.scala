package kaimere.real.optimization.general.instructions

import kaimere.real.optimization.general.OptimizationAlgorithm
import spray.json._

trait Instruction {

  def continue(algorithm: OptimizationAlgorithm): Boolean
  def reset(): Unit
  def onQuit(algorithm: OptimizationAlgorithm): Unit = {}

}

object Instruction {

  def fromCsv(csv: String): Instruction = {
    val name = csv.split(",").head
    name match {
      case "AllInstruction" => AllInstruction(csv)
      case "AnyInstruction" => AnyInstruction(csv)
      case "MaxIterations" => MaxIterations(csv)
      case "MaxTime" => MaxTime(csv)
      case "StateLogger" => StateLogger(csv)
      case "TargetValue" => TargetValue(csv)
      case "VerboseBest" => VerboseBest(csv)
      case _ => throw DeserializationException(s"Unsupported Instruction: $name")
    }
  }

  def toJson(instruction: Instruction): JsValue = {
    instruction match {
      case mi: MaxIterations => mi.toJson
      case mt: MaxTime => mt.toJson
      case tv: TargetValue => tv.toJson
      case vb: VerboseBest => vb.toJson
      case sl: StateLogger => sl.toJson
      case all_i: AllInstruction => all_i.toJson
      case any_i: AnyInstruction => any_i.toJson
      case _ => throw new Exception(s"Unsupported Instruction: ${instruction.toString}")
    }
  }

  def fromJson(json: JsValue): Instruction = {
    json.asJsObject.getFields("name") match {
      case Seq(JsString(name)) =>
        name match {
          case "MaxIterations" => json.convertTo[MaxIterations]
          case "MaxTime" => json.convertTo[MaxTime]
          case "TargetValue" => json.convertTo[TargetValue]
          case "VerboseBest" => json.convertTo[VerboseBest]
          case "StateLogger" => json.convertTo[StateLogger]
          case "AllInstruction" => json.convertTo[AllInstruction]
          case "AnyInstruction" => json.convertTo[AnyInstruction]
          case _ => throw DeserializationException(s"Unsupported Instruction: ${name}")
        }
      case _ => throw DeserializationException("Instruction expected")
    }
  }

}