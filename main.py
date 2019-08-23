import blackjack

game = blackjack.Blackjack()




def main():
    game.deal()

    while not game.gameover:
        game.printState()
        print("Would you like to hit? [y/n]")
        ans = input()

        if ans == "y":
            game.hit()
            game.checkGameover()
        elif ans == 'n':
            game.finished = True
            game.printState()
            stopped = False
            while not stopped:

                if game.getDealerTotal() > 21:
                    print("Congratulations you win")
                    stopped = True
                elif game.getDealerTotal() > 17:
                    stopped = true
                    if game.getPlayerTotal() > game.getDealerTotal():
                        print("Congratulations you win")
                    elif game.getPlayerTotal() == game.getDealerTotal():
                        print("Push")
                    elif game.getPlayerTotal() < game.getDealerTotal():
                        print("You lose")
                elif game.getDealerTotal() < 17:
                    game.hitDealer()
                    game.printState()
                    
            break

if __name__ == "__main__":
    main()
