import java.io._

object Solution {

    def sockMerchant(n: Int, ar: Array[Int]): Int = {
        ar.groupBy(identity).values.map(_.size / 2).sum
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn
        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))
        val n = stdin.readLine.trim.toInt
        val ar = stdin.readLine.split(" ").map(_.trim.toInt)
        val result = sockMerchant(n, ar)
        printWriter.println(result)
        printWriter.close()
    }
}
