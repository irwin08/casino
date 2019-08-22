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

            if game.printDealerTotal() > 21:
                print("Congratulations you win")
                break
            
            
            break

if __name__ == "__main__":
    main()
