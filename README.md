Задача
Создать систему для вычисления стоимости разработческих услуг (тарификация - почасовая, помесячная, позадачная).

Как залогиненный пользователь я могу:
Создать проект - название и описание.
Задать рейт своих услуг в час для созданного проекта.
Указать свою тарифную ставку для созданного проекта (способ начисления оплаты - почасовая, помесячная, позадачная). Если тарифная ставка почасовая, то счет на оплату могу выставить в любой момент, после указания времени и даты окончания работ. Если тарифная ставка помесячная, то счет на оплату могу выставить только за предыдущие месяцы. Если тарифная ставка позадачная, то счет на оплату могу выставить только после указания, что задача выполнена.
Указать время и дату начала работы над созданным проектом.
Указать время и дату окончания работы над созданным проектом.
Создать счет на оплату по созданному проекту, в котором будет указываться название проекта, тарифная ставка, отработанный период времени и автоматически вычисляться стоимость услуг на основании отработанных часов и установленного рейта. 
Сохранять  счет на оплату в PDF формате.



Технические подробности

Одним из основных технических требований к системе является отсутствие логики во вью классах (чтобы не было расчетов во вьюшках).
