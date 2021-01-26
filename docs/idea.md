# Vorschlag für die Main-Loop

Die Klassen werden jeweils in sepparaten Files definiert

    import Gamelogic
    import Display
    import Inputhandler

Der Inputhandler läuft im Hintergrund und merkt sich alle Tastendrücke

    input_handler = Inputhandler.init()

game enthält die gesamte Logik des Spiels

    game = Gamelogic.init()

Das Display Objekt erledigt die Anzeige des Spiels

    display = Display.init()

Hauptschleife

        while (game.is_running):

Die gesammelten Tastenanschläge werden vom inputhandler übernommen

            pressed_buttons = input_handler.get_input()

Das Spiel wird mit den Tastenanschlägen geupdated

            game.update(pressed_buttons)

Die neu generierte Anzeige wird von der Spiellogik übernommen

            screen_buffer = game.get_screen_buffer()

Die Anzeige wird als ASCII auf der Konsole angezeigt oder als LED Matrix auf dem "Gameboy"

            display.draw(screen_buffer)
