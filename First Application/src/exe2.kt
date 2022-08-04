fun main(){
    val idade = 100
    val camadas = 10
    printcakeCandles(idade)
    printcakeTop(idade)
    printcakeBottom(idade, camadas)
}

fun printcakeTop(idade: Int){
    repeat(idade){
        print("*")
    }
    println()
}

fun printcakeCandles(idade: Int){
    repeat(idade){
        print("`")
    } 
    println()

    repeat(idade){
        print("|")
    } 
    println()
}
fun printcakeBottom(idade: Int, camadas: Int){
    repeat(camadas){
        repeat(idade){
            print("@")
        }
        println()
    }
}