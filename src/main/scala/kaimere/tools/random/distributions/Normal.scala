package kaimere.tools.random.distributions

trait Normal {

  def getNormal(mu: Double, sigma: Double): Double

  final def getNormal(area: Map[String, (Double, Double)]): Map[String, Double] =
    area.map { case (key, (mu, sigma)) => (key, getNormal(mu, sigma)) }

}