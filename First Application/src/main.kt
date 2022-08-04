fun main(){

    val borda = ":"
    val repeat = 6

    /* FIRST IMPLEMENTACION
    var idade = 20 * 365
    var name = "Taisy"

    println("Happy Birthday!")
    println("${name},")
    println("You are ${idade} days old, ${name}!")

    println("   ,,,,,   ")
    println("   |||||   ")
    println(" =========")
    println("@@@@@@@@@@@")
    println("{~@~@~@~@~}")
    println("@@@@@@@@@@@")
    println("") 
    */
    
    printBorder(borda, repeat)
    println("Happy Birthday, Taisy!")
    printBorder(borda, repeat)
}

fun printBorder(borda: String, repeat: Int){
    repeat(repeat){
        print(borda)
    }
    println()
}