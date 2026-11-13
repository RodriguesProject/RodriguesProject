// Exemplos de consultas MongoDB sobre documentos inteiramente fictícios.
// 1. Demandas em andamento
 db.demandas.find({ status: "Em andamento" });

// 2. Contagem por área
 db.demandas.aggregate([
   { $match: { status: "Em andamento" } },
   { $group: { _id: "$area", quantidade: { $sum: 1 } } },
   { $sort: { quantidade: -1 } }
 ]);

// 3. Soma de valores referenciais por área
 db.demandas.aggregate([
   { $group: { _id: "$area", valor_referencial: { $sum: "$valor_referencia_brl" } } },
   { $sort: { valor_referencial: -1 } }
 ]);
