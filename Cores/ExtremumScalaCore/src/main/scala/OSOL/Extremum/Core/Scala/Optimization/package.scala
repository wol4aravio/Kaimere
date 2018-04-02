package OSOL.Extremum.Core.Scala

package object Optimization {

  type Area = Map[String, (Double, Double)]

  object Exceptions {

    class ParameterAlreadyExistsException(parameterName: String) extends Exception
    class NoSuchParameterException(parameterName: String) extends Exception

  }

}
