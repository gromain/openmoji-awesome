package io.bazile.openmojiamazing

import com.beust.klaxon.Klaxon
import java.io.File
import java.net.URL

fun openmojiColorUrl(unicode: String) = "https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@12.3.0/color/svg/$unicode.svg"
fun openmojiBlackUrl(unicode: String) = "https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@12.3.0/black/svg/$unicode.svg"

data class Emoji(val hexcode: String, val annotation: String)

fun main(args: Array<String>) {
    val preamble = File("preamble.css")
    val preambleLines = preamble.readLines()
    val json = URL("https://raw.githubusercontent.com/hfg-gmuend/openmoji/12.3.0/data/openmoji.json").readText()
    val result = Klaxon().parseArray<Emoji>(json) ?: listOf()
    val new = result.filter {
        it.annotation.all { it.isLetter() || it == ' ' || it == '-' || it == ':' }
    }.map {
        Emoji(it.hexcode.toUpperCase().split(" ").joinToString("-"), it.annotation.toLowerCase().split(" ").joinToString("-").replace(":", ""))
    }
    val cssColorClasses = new.map {
        """
            .oma-${it.annotation} {
                background-image: url("${openmojiColorUrl(it.hexcode)}")
            }
        """.trimIndent()
    }
    val cssBlackClasses = new.map {
        """
            .oma-black-${it.annotation} {
                background-image: url("${openmojiBlackUrl(it.hexcode)}")
            }
        """.trimIndent()
    }
    println("Generated a total of ${new.count()} emoji CSS classes.")
    File("openmoji-color-awesome.css").printWriter().use { out ->
        preambleLines.forEach {
            out.println(it)
        }
        out.println("""
        
        /* Generated a total of ${new.count()} emoji CSS classes. */
        
        """.trimIndent())
        cssColorClasses.forEach {
            out.println(it)
        }
    }
    File("openmoji-black-awesome.css").printWriter().use { out ->
        preambleLines.forEach {
            out.println(it)
        }
        out.println("""
        
        /* Generated a total of ${new.count()} emoji CSS classes. */
        
        """.trimIndent())
        cssBlackClasses.forEach {
            out.println(it)
        }
    }
}
