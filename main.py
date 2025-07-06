def runthething(event):
 win1 = document.querySelector('#win1')
 win2 = document.querySelector('#win2')
 lose1 = document.querySelector('#lose1')
 lose2 = document.querySelector('#lose2')

 bestwin = float(max(win1, win2))
 bestloss = float(max(lose1, lose2))

 arbitrage = ((1/bestwin) + (1/bestloss))
 score=(100-(arbitrage*100))
 if score<0:
   print('There is no possible arbitrage with these odds.')

 else:
   print(score,'% is our profit margin.')
   amount = float(input('How much are you looking to bet? '))
   profit = (amount/arbitrage) - amount
   percentageprofit = (profit/amount)*100
   print('$',profit,'is your guaranteed profit, or a return of',percentageprofit,'%.')
   winstake = (amount*(1/bestwin))/arbitrage
   lossstake = (amount*(1/bestloss))/arbitrage

   print('Place a bet of $',winstake,'for a win.')
   print('Place a bet of $',lossstake,'for a loss.')



