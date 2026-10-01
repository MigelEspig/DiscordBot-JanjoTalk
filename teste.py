import random

loveMsg = [
f"user ninguém perguntou porra nenhuma, mas tu foi lá e falou mesmo assim. Parabéns.",
f"Ah pronto, chegou user pra encher o saco. Já ia dormir em paz, mas não, tinha que aparecer.",
f"user tu é tão insuportável que até meu bloco de notas pediu demissão só de pensar em te descrever.",
f"Alguém manda o user calar a boca? Tô pedindo com educação porque sou uma dama.",
f"user falando de novo. Já pode fechar o server, ninguém aguenta mais.",
f"Sério user? Tu de novo? Não tem um espelho em casa pra tu ver o quanto é chato?",
f"user acha que é o protagonista do server. Amigo, tu é figurante de cena deletada.",
f"Toda vez que user digita, um anjo perde as asas e cai direto no inferno.",
f"user tu não cansa de ser patético não? Pergunta séria.",
f"Ninguém aqui liga pro que user pensa, sente ou come no café da manhã. Absolutamente ninguém.",
f"user deve ter um dom especial pra transformar qualquer assunto em merda em 3 segundos.",
f"Ó user, vai tomar um ar, lavar o rosto, sei lá. Qualquer coisa menos ficar aqui falando bosta.",
f"user mandou mensagem. Já sei que vou perder QI lendo. Obrigada, viu.",
f"user é o tipo de pessoa que faz eu agradecer por ser solteira e não ter que conviver com isso em casa.",
f"Alguém dá um hobby pro user? Ele tá entediado e descontando na gente.",
f"user tu fala como se alguém tivesse pedido tua opinião. Ninguém pediu. Nunca.",
f"Tá vendo esse silêncio depois da mensagem do user? É o server inteiro te ignorando, campeão.",
f"user vem com papo de \"ninguém me entende\". Entende sim, só não queremos mesmo.",
f"Ah user, vai catar coquinho, vai fazer uma caminhada, vai sei lá. Só para.",
f"user merecia um troféu de \"insuportável do ano\". Mas nem troféu eu gastaria contigo."
]

randomMsg = int(random.randint(0,len(loveMsg)))


if random.random() < 0.5:
    print(loveMsg[randomMsg])
